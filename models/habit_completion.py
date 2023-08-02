from db import db


class HabitCompletionModel(db.Model):
    __tablename__ = "habit_completions"

    id = db.Column(db.Integer, primary_key=True)
    habit_id = db.Column(db.Integer, db.ForeignKey("habits.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    # maybe instead of date and is_completed, just have a date_completed field
    date = db.Column(db.Date, nullable=False)
    is_completed = db.Column(db.Boolean, default=False)

    # Define the many-to-one relationship with Habit
    # habit = db.relationship("HabitModel", back_populates="records")

    def __repr__(self):
        return f"<HabitCompletionModel(date='{self.date}', is_completed='{self.is_completed}')>"
