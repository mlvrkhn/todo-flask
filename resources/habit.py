from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores

bp = Blueprint("habit", __name__, description="Operations on habits")


@bp.route("/habits/<string:store_id>")
class Habit(MethodView):
    def get(self, store_id):
        return {"message": "testing getting habit going on..."}

    def delete(self, store_id):
        pass
