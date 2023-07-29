from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import UserSchema
import uuid


bp = Blueprint("user", __name__, description="Operations on users")

users = {}


@bp.route("/users")
class Users(MethodView):
    @bp.response(200, UserSchema(many=True))
    def get(self):
        try:
            return users.values()
        except KeyError:
            abort(404, message="Users dont 't exist")

    @bp.arguments(UserSchema)
    def post(self, user_data):
        try:
            user_id = uuid.uuid4().hex
            user_data = {"id": user_id, **user_data}
            users[user_id] = user_data
            return user_data, 201
        except KeyError:
            # if user exists?
            abort(404, message="User dont't exist")


@bp.route("/users/<string:user_id>")
class User(MethodView):
    def get(self, user_id):
        try:
            return users[user_id]
        except KeyError:
            abort(404, message="User {} doesn't exist".format(user_id))

    @bp.arguments(UserSchema)
    def put(self, user_data, user_id):
        print("user_data", user_data, user_id)
        try:
            users[user_id] = user_data
            return users[user_id], 200
        except KeyError:
            abort(404, message="User {} doesn't exist".format(user_id))

    def delete(self, user_id):
        try:
            del users[user_id]
            return "", 204
        except KeyError:
            abort(404, message="User not found")
