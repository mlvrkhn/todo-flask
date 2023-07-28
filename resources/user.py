from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import UserSchema


bp = Blueprint("user", __name__, description="Operations on users")

users = {
    6: {
        "id": 6,
        "username": "JEDZENIE",
    }
}


@bp.route("/users")
@bp.route("/users/<int:user_id>")
class User(MethodView):
    def get(self, user_id):
        try:
            return users[user_id]
        except KeyError:
            abort(404, message="User {} doesn't exist".format(user_id))

    @bp.arguments(UserSchema)
    def post(self, user_data):
        print("user_data", user_data)

    # @bp.arguments(UpdateUserSchema)
    # def put(self, user_id):
    #     pass

    def delete(self, user_id):
        pass
