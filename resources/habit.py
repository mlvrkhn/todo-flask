from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import PlainHabitSchema, HabitSchema
from models import HabitModel

from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db

bp = Blueprint("habit", __name__, description="Operations on habits")


@bp.route("/habits")
class Habit(MethodView):
    @bp.response(200, HabitSchema(many=True))
    def get(self):
        return HabitModel.query.all()

    @bp.arguments(HabitSchema)
    @bp.response(201, HabitSchema)
    def post(self, habit_data):
        try:
            habit = HabitModel(**habit_data)
            print("🚀   habit:", habit)
            db.session.add(habit)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Habit already exists")
        except SQLAlchemyError:
            abort(500, message="Error occured while creating habit")

        return habit


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
        habit = HabitModel.query.get(habit_id)
        if habit:
            db.session.delete(habit)
            db.session.commit()
            return {"message": "Habit deleted successfully"}
        else:
            abort(404, message="Habit not found")
