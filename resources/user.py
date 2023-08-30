from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import PlainUserSchema, UserSchema, HabitSchema, LoginSchema
from passlib.hash import pbkdf2_sha256 as sha256
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt,
    create_refresh_token,
    get_jwt_identity,
)

from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from models import UserModel
from db import db

from blocklist import BLOCKLIST

bp = Blueprint("user", __name__, description="Operations on users")


@bp.route("/test")
class UserRegister(MethodView):
    @bp.arguments(UserSchema)
    def post(self, user_data):
        # print("test", request.get_json())
        print("test", user_data)
        return {"message": "User created successfully."}, 201


@bp.route("/register")
class UserRegister(MethodView):
    @bp.arguments(PlainUserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(409, message="A user with that username already exists.")

        user = UserModel(
            username=user_data["username"],
            email=user_data["email"],
            password=sha256.hash(user_data["password"]),
        )

        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully."}, 201


@bp.route("/login")
class UserLogin(MethodView):
    @bp.arguments(LoginSchema)
    def post(self, user_data):
        user = UserModel.query.filter_by(username=user_data["username"]).first()

        if user and sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}, 200
        else:
            abort(401, message="Invalid credentials.")


@bp.route("/refresh")
class TokenRefresh(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        user_id = get_jwt_identity()
        new_token = create_access_token(identity=user_id, fresh=False)
        return {"access_token": new_token}, 200


@bp.route("/logout")
class UserLogin(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message": "Successfully logged out."}, 200


@bp.route("/users/<int:user_id>")
class User(MethodView):
    @bp.response(200, UserSchema)
    def get(self, user_id):
        return UserModel.find_by_user_id(user_id)

    def delete(self, user_id):
        user = UserModel.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted successfully"}


@bp.route("/users/<string:user_id>/habits")
class User(MethodView):
    @bp.response(200, HabitSchema(many=True))
    def get(self, user_id):
        try:
            user = UserModel.query.get(user_id)
            return user.habits
        except KeyError:
            abort(404, message="Habits for {} don't exist".format(user_id))
