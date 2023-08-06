from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    # Define a one-to-many relationship with Habit
    habits = db.relationship(
        "HabitModel", back_populates="user", cascade="all, delete", lazy="dynamic"
    )

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"
