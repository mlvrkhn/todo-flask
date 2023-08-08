from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import PlainHabitSchema, HabitSchema, UpdateHabitSchema
from models import HabitModel
from flask_jwt_extended import jwt_required

from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db

bp = Blueprint("habit", __name__, description="Operations on habits")


@bp.route("/habits")
class Habit(MethodView):
    @bp.response(200, HabitSchema(many=True))
    def get(self):
        return HabitModel.query.all()

    @jwt_required()
    @bp.arguments(HabitSchema)
    @bp.response(201, HabitSchema)
    def post(self, habit_data):
        try:
            habit = HabitModel(**habit_data)
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
        return HabitModel.query.get_or_404(habit_id)

    @jwt_required()
    @bp.arguments(UpdateHabitSchema)
    @bp.response(200, HabitSchema)
    def put(self, update_data, habit_id):
        try:
            habit = HabitModel.query.get(habit_id)
            if habit is None:
                abort(404, message="Item not found.")
            for key, value in update_data.items():
                setattr(habit, key, value)
            db.session.commit()
            return habit
        except SQLAlchemyError:
            abort(500, message="Error updating item.")

    @jwt_required()
    def delete(self, habit_id):
        habit = HabitModel.query.get(habit_id)
        if habit:
            db.session.delete(habit)
            db.session.commit()
            return {"message": "Habit deleted successfully"}
        else:
            abort(404, message="Habit not found")
