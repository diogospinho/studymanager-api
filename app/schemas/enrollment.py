from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.schemas.course import CourseOut
from app.schemas.user import UserOut


class EnrollmentCreate(BaseModel):
    user_id: int
    course_id: int


class EnrollmentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    course_id: int
    enrolled_at: datetime


class UserCoursesOut(BaseModel):
    user: UserOut
    courses: list[CourseOut]
