from db import db
from sqlalchemy.orm import relationship

# from models import DailyRecordModel


class HabitModel(db.Model):
    __tablename__ = "habits"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255))
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)

    # Define a one-to-many relationship with DailyRecord
    records = db.relationship(
        "DailyRecordModel", back_populates="habit", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<HabitModel(name='{self.name}', user_id='{self.user_id}', start_date='{self.start_date}')>"
