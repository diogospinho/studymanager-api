from sqlalchemy import select
from sqlalchemy.orm import Session

from app.entities.course import Course


class CourseRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, course: Course) -> Course:
        self.db.add(course)
        self.db.commit()
        self.db.refresh(course)
        return course

    def get_all(self) -> list[Course]:
        stmt = select(Course).order_by(Course.id)
        return list(self.db.scalars(stmt).all())

    def get_by_id(self, course_id: int) -> Course | None:
        stmt = select(Course).where(Course.id == course_id)
        return self.db.scalar(stmt)

    def update(self, course: Course) -> Course:
        self.db.commit()
        self.db.refresh(course)
        return course

    def delete(self, course: Course) -> None:
        self.db.delete(course)
        self.db.commit()
