from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import PlainUserSchema, UserSchema, HabitSchema

import uuid

from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from models import UserModel
from db import db

bp = Blueprint("user", __name__, description="Operations on users")


@bp.route("/users")
class Users(MethodView):
    @bp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

    @bp.arguments(UserSchema)
    @bp.response(201, UserSchema)
    def post(self, user_data):
        try:
            user = UserModel(**user_data)
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message="User already exists")
        except SQLAlchemyError:
            abort(500, message="Error occured while creating user")

        return user


@bp.route("/users/<string:user_id>")
class User(MethodView):
    @bp.response(200, UserSchema)
    def get(self, user_id):
        return UserModel.query.get_or_404(user_id)

    @bp.arguments(PlainUserSchema)
    @bp.response(200, UserSchema)
    def put(self, user_data, user_id):
        user = UserModel.get_by_id(user_id)
        if user:
            user.username = user_data["username"]
            user.email = user_data["email"]
            user.password = user_data["password"]
        else:
            item = UserModel(id=user_id, **user_data)

        db.session.add(user)
        db.session.commit()

        return user

    def delete(self, user_id):
        user = UserModel.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {"message": "User deleted successfully"}
        else:
            abort(404, message="User not found")


@bp.route("/users/<string:user_id>/habits")
class User(MethodView):
    @bp.response(200, HabitSchema(many=True))
    def get(self, user_id):
        try:
            user = UserModel.query.get(user_id)
            return user.habits
        except KeyError:
            abort(404, message="Habits for {} don't exist".format(user_id))
