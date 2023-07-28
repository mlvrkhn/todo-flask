from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores

bp = Blueprint("stores", __name__, description="Operations on stores")


@bp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        pass

    def delete(self, store_id):
        pass
