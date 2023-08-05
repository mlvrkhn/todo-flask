from db import db
from sqlalchemy.orm import relationship


class HabitCompletionModel(db.Model):
    __tablename__ = "habit_completions"

    id = db.Column(db.Integer, primary_key=True)
    habit_id = db.Column(db.String, db.ForeignKey("habits.id"), nullable=False)
    completion_date = db.Column(db.Date, nullable=False, default=db.func.current_date())
    habit = relationship("HabitModel", back_populates="completions")

    def __repr__(self):
        return f"<HabitCompletionModel(completion_date='{self.completion_date}')>"
