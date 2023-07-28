from db import db


class DailyRecordModel(db.Model):
    __tablename__ = "daily_records"

    id = Column(Integer, primary_key=True)
    habit_id = Column(Integer, ForeignKey("habits.id"), nullable=False)
    date = Column(Date, nullable=False)
    is_completed = Column(Boolean, default=False)
    notes = Column(String(255))

    # Define the many-to-one relationship with Habit
    habit = relationship("HabitModel", back_populates="records")

    def __repr__(self):
        return f"<DailyRecordModel(date='{self.date}', is_completed='{self.is_completed}')>"
