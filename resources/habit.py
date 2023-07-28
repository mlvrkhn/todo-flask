from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import HabitSchema

bp = Blueprint("habit", __name__, description="Operations on habits")

habits = {}


@bp.route("/habits/<string:store_id>")
class Habit(MethodView):
    def get(self, habit_id):
        try:
            return habits[habit_id]
        except KeyError:
            abort(404, message="User {} doesn't exist".format(habit_id))

    @bp.arguments(HabitSchema)
    def post(self, habit_data):
        print("habit_data", habit_data)

    # @bp.arguments(HabitUpdateSchema)
    # def put(self, habit_id):
    #     pass

    def delete(self, habit_id):
        pass
