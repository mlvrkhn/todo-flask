from marshmallow import Schema, fields


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
    start_date = fields.Date(required=True)
    end_date = fields.Date()


class HabitSchema(PlainHabitSchema):
    id = fields.Int(dump_only=True)
    records = fields.Nested(PlainDailyRecordSchema(), many=True)
    # records = fields.Nested(PlainDailyRecordSchema(), many=True, exclude=("habit",))


class PlainUserSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)


class UserSchema(PlainUserSchema):
    id = fields.Str(dump_only=True)
    habits = fields.List(fields.Nested(PlainHabitSchema()), dump_only=True)


# class HabitUpdateSchema(Schema):
#     id = fields.Int(dump_only=True)
#     user_id = fields.Int(required=True)
#     name = fields.Str(required=True)
#     description = fields.Str()
#     start_date = fields.Date(required=True)
#     end_date = fields.Date()
#     records = fields.Nested(DailyRecordSchema, many=True, exclude=("habit",))

# class UpdateUserSchema(Schema):
#     id = fields.Int(dump_only=True)
#     username = fields.Str(required=True)
#     email = fields.Email(required=True)
#     password = fields.Str(required=True, load_only=True)
#     habits = fields.Nested("HabitSchema", many=True, exclude=("user",))
