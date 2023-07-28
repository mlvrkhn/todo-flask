from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


""" from pony.orm import Database, Required, Optional, Set, PrimaryKey
from datetime import datetime
from flask_smorest import Blueprint, abort

db = Database()


# change methods to use smokest
class User(db.Entity):
    token = Optional(str, nullable=True)
    username = Required(str, unique=True)
    password = Required(str)
    last_login = Optional(datetime)
    tasks = Set("Task", reverse="user")

    def __repr__(self):
        return "<User {}>".format(self.username)


class Task(db.Entity):
    title = Required(str)
    description = Optional(str)
    created = Required(datetime, default=datetime.now)
    updated = Optional(datetime, default=datetime.now)
    status = Required(str, default="new")
    user = Required(User)


class Store(db.Entity):
    name = Required(str)
    items = Set("Item", reverse="store")


# stores = {}
# items = {
#     1: {"name": "Chair", "price": 15.99},
#     2: {"name": "Desk", "price": 25.99},
# }
# todos = {
#     1: {
#         "task": "todo",
#         "store_id": 1,
#     },
# }
 """
