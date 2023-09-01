from db import db
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime


class HabitModel(db.Model):
    __tablename__ = "habits"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255))
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    user = relationship("UserModel", back_populates="habits")
    completions = relationship("HabitCompletionModel", back_populates="habit")

    def __repr__(self):
        return f"<HabitModel(name='{self.name}', user_id='{self.user_id}', start_date='{self.start_date}')>"
