from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
    # habits = fields.Nested(HabitSchema, many=True, exclude=("user",))


# class UpdateUserSchema(Schema):
#     id = fields.Int(dump_only=True)
#     username = fields.Str(required=True)
#     email = fields.Email(required=True)
#     password = fields.Str(required=True, load_only=True)
#     habits = fields.Nested("HabitSchema", many=True, exclude=("user",))


class DailyRecordSchema(Schema):
    id = fields.Int(dump_only=True)
    habit_id = fields.Int(required=True)
    date = fields.Date(required=True)
    is_completed = fields.Boolean(missing=False)
    notes = fields.Str()


class HabitSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str()
    start_date = fields.Date(required=True)
    end_date = fields.Date()
    # records = fields.Nested(DailyRecordSchema, many=True, exclude=("habit",))


# class HabitUpdateSchema(Schema):
#     id = fields.Int(dump_only=True)
#     user_id = fields.Int(required=True)
#     name = fields.Str(required=True)
#     description = fields.Str()
#     start_date = fields.Date(required=True)
#     end_date = fields.Date()
#     records = fields.Nested(DailyRecordSchema, many=True, exclude=("habit",))
