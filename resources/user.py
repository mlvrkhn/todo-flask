from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import UserSchema
import uuid


bp = Blueprint("user", __name__, description="Operations on users")

users = {
    "6": {
        "id": 6,
        "username": "JEDZENIE",
    }
}


@bp.route("/users")
class Users(MethodView):
    def get(self):
        try:
            return {"users": users}
        except KeyError:
            abort(404, message="User dont 't exist")

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


@bp.route("/users/<int:user_id>")
class User(MethodView):
    def get(self, user_id):
        try:
            return users[user_id]
        except KeyError:
            abort(404, message="User {} doesn't exist".format(user_id))

    @bp.arguments(UserSchema)
    def put(self, user_data):
        print("user_data", user_data)

    def delete(self, user_id):
        pass
