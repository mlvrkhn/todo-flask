from db import db


class HabitModel(db.Model):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(100), unique=true, nullable=False)
    description = Column(String(255))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)

    # Define a one-to-many relationship with DailyRecord
    records = relationship(
        "DailyRecordModel", back_populates="habit", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<HabitModel(name='{self.name}', user_id='{self.user_id}', start_date='{self.start_date}')>"
