from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import (
    PlainHabitSchema,
    HabitSchema,
    HabitCompletionSchema,
    PlainHabitCompletionSchema,
)
from models import HabitCompletionModel, HabitModel

from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db

bp = Blueprint("habit_completion", __name__, description="Habit completion operations")


@bp.route("/completions")
class HabitCompletion(MethodView):
    @bp.response(200, HabitCompletionSchema(many=True))
    def get(self):
        return HabitCompletionModel.query.all()

    @bp.arguments(HabitCompletionSchema)
    @bp.response(201, HabitCompletionSchema)
    def post(self, habit_completion_data):
        try:
            completion = HabitCompletionModel.query.filter_by(
                habit_id=habit_completion_data["habit_id"],
                completion_date=habit_completion_data["completion_date"],
            ).first()

            if completion is None:
                new_completion = HabitCompletionModel(**habit_completion_data)
                db.session.add(new_completion)
                db.session.commit()
            else:
                abort(400, message="Habit completion already exists")

        except IntegrityError:
            abort(404, message="Habit not found")

        return new_completion


@bp.route("/completions/<string:completion_id>")
class HabitCompletion(MethodView):
    @bp.response(200, HabitCompletionSchema)
    def get(self, completion_id):
        return HabitCompletionModel.query.get_or_404(completion_id)

    @bp.arguments(PlainHabitCompletionSchema)
    @bp.response(201, HabitCompletionSchema)
    def put(self, habit_completion_data, completion_id):
        new_completion = HabitCompletionModel(**habit_completion_data)
        try:
            db.session.add(new_completion)
            db.session.commit()
        except SQLAlchemyError:
            abort(404, message="Habit not found")

        return new_completion
