from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import PlainHabitSchema, HabitSchema

bp = Blueprint("habit", __name__, description="Operations on habits")

habits = {}


@bp.route("/habits")
class Habit(MethodView):
    @bp.response(200, HabitSchema(many=True))
    def get(self):
        try:
            return habits.values()
        except KeyError:
            abort(404, message="Users dont 't exist")

    @bp.arguments(PlainHabitSchema)
    @bp.response(201, HabitSchema)
    def post(self, habit_data):
        try:
            habit_id = uuid.uuid4().hex
            habit_data = {"id": habit_id, **habit_data}
            habits[habit_id] = habit_data
            return habit_data, 201
        except KeyError:
            abort(404, message="Habit dont't exist")


@bp.route("/habits/<string:habit_id>")
class Habit(MethodView):
    @bp.response(200, HabitSchema)
    def get(self, habit_id):
        try:
            return habits[habit_id]
        except KeyError:
            abort(404, message="Habit {} doesn't exist".format(habit_id))

    @bp.arguments(PlainHabitSchema)
    @bp.response(200, HabitSchema)
    def post(self, habit_data):
        print("habit_data", habit_data)
        # TOOD

    def delete(self, habit_id):
        try:
            del habits[habit_id]
            return "", 204
        except KeyError:
            abort(404, message="Habit not found")
