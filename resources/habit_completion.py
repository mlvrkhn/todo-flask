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


@bp.route("/completions", methods=["GET", "POST"])
class HabitCompletion(MethodView):
    @bp.response(200, HabitCompletionSchema(many=True))
    def get(self):
        return HabitCompletionModel.query.all()

    @bp.arguments(PlainHabitCompletionSchema)
    @bp.response(201, HabitCompletionSchema)
    def post(self, habit_completion_data):
        try:
            # if "completion_date" not in habit_completion_data:
            #     return jsonify({"error": "completion_date is required"}), 400

            # Check if the completion already exists for the given date and habit_id
            # Create a new habit completion
            new_completion = HabitCompletionModel(**habit_completion_data)
            db.session.add(new_completion)
            db.session.commit()

        except IntegrityError:
            db.session.rollback()
            abort(404, message="Habit not found")
        # except Exception as e:
        #     db.session.rollback()
        #     print("🚀   e:", e)
        #     abort(404, message="An error occured while creating habit completion")

        return new_completion


@bp.route("/completions/<string:completion_id>", methods=["GET", "POST"])
class HabitCompletion(MethodView):
    @bp.response(200, HabitCompletionSchema(many=True))
    def get(self, completion_id):
        return HabitCompletionModel.query.get_or_404(completion_id)

    @bp.arguments(PlainHabitCompletionSchema)
    @bp.response(201, HabitCompletionSchema)
    def post(self, habit_completion_data, completion_id):
        try:
            # if "completion_date" not in habit_completion_data:
            new_completion = HabitCompletionModel(**habit_completion_data)
            db.session.add(new_completion)
            db.session.commit()
        except SQLAlchemyError:
            abort(404, message="Habit not found")
        # except Exception as e:
        #     db.session.rollback()
        #     print("🚀   e:", e)
        #     abort(404, message="An error occured while creating habit completion")

        return new_completion


# def put(self, update_data, pet_id):
#         """Update existing pet"""
#         try:
#             item = Pet.get_by_id(pet_id)
#         except ItemNotFoundError:
#             abort(404, message="Item not found.")
#         item.update(update_data)
#         item.commit()
#         return item
