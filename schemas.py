from marshmallow import Schema, fields
from datetime import datetime


class PlainDailyRecordSchema(Schema):
    habit_id = fields.Int(required=True)
    date = fields.Date(required=True)
    # is_completed = fields.Boolean(missing=False)
    notes = fields.Str()


class DailyRecordSchema(PlainDailyRecordSchema):
    id = fields.Int(dump_only=True)


class PlainHabitSchema(Schema):
    user_id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str()
    start_date = fields.Date()
    end_date = fields.Date()


class HabitSchema(PlainHabitSchema):
    id = fields.Int(dump_only=True)
    records = fields.Nested(PlainDailyRecordSchema(), many=True)
    # records = fields.Nested(PlainDailyRecordSchema(), many=True, exclude=("habit",))


class UpdateHabitSchema(Schema):
    name = fields.Str()
    description = fields.Str()


class PlainUserSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)


class UserSchema(PlainUserSchema):
    id = fields.Str(dump_only=True)
    habits = fields.List(fields.Nested(PlainHabitSchema()), dump_only=True)


class PlainHabitCompletionSchema(Schema):
    habit_id = fields.Str(required=True)
    completion_date = fields.Date(default=datetime.utcnow)


class HabitCompletionSchema(PlainHabitCompletionSchema):
    id = fields.Int(dump_only=True)
