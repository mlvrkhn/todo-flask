from db import db
from sqlalchemy.orm import relationship
from datetime import datetime


class HabitModel(db.Model):
    __tablename__ = "habits"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255))
    start_date = db.Column(db.Date, nullable=True, default=datetime.utcnow)
    # end_date = db.Column(db.Date)

    user = db.relationship("UserModel", back_populates="habits")
    records = db.relationship(
        "HabitCompletionModel", back_populates="habit", cascade="all, delete"
    )

    def __repr__(self):
        return f"<HabitModel(name='{self.name}', user_id='{self.user_id}', start_date='{self.start_date}')>"
