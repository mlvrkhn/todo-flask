from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

bp = Blueprint("user", __name__, description="Operations on users")


@bp.route("/users/<string:user_id>")
class Habit(MethodView):
    def get(self, user_id):
        try:
            return stores[user_id]
        except KeyError:
            abort(404, message="User {} doesn't exist".format(user_id))

    def delete(self, user_id):
        pass
