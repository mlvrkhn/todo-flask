from marshmallow import Schema, fields
from datetime import datetime


class PlainDailyRecordSchema(Schema):
    habit_id = fields.Int(required=True)
    completion_date = fields.Date(required=True)


class DailyRecordSchema(PlainDailyRecordSchema):
    id = fields.Int(dump_only=True)


class PlainHabitSchema(Schema):
    user_id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str()
    time_created = fields.Date()
    time_updated = fields.Date()


class HabitSchema(PlainHabitSchema):
    id = fields.Int(dump_only=True)
    completions = fields.Nested(DailyRecordSchema(), many=True)


class UpdateHabitSchema(Schema):
    name = fields.Str()
    description = fields.Str()


class RegistrationSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)


class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    habits = fields.List(fields.Nested(HabitSchema()))


class PlainUserSchema(UserSchema):
    username = fields.Str(dump_only=True)
    email = fields.Email(dump_only=True)
    password = fields.Str(dump_only=True)


class PlainHabitCompletionSchema(Schema):
    habit_id = fields.Str(required=True)
    completion_date = fields.Date(default=datetime.utcnow)


class HabitCompletionSchema(PlainHabitCompletionSchema):
    id = fields.Int(dump_only=True)
