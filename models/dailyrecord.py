from db import db


class DailyRecordModel(db.Model):
    __tablename__ = "daily_records"

    id = db.Column(db.Integer, primary_key=True)
    habit_id = db.Column(db.Integer, db.ForeignKey("habits.id"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    is_completed = db.Column(db.Boolean, default=False)
    notes = db.Column(db.String(255))

    # Define the many-to-one relationship with Habit
    habit = db.relationship("HabitModel", back_populates="records")

    def __repr__(self):
        return f"<DailyRecordModel(date='{self.date}', is_completed='{self.is_completed}')>"
