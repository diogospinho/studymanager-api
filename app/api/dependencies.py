from fastapi import Depends
from sqlalchemy.orm import Session

from app.infrastructure.database import get_db
from app.repositories.course_repository import CourseRepository
from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.user_repository import UserRepository
from app.services.course_service import CourseService
from app.services.enrollment_service import EnrollmentService
from app.services.user_service import UserService


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repository = UserRepository(db)
    return UserService(repository)


def get_course_service(db: Session = Depends(get_db)) -> CourseService:
    repository = CourseRepository(db)
    return CourseService(repository)


def get_enrollment_service(db: Session = Depends(get_db)) -> EnrollmentService:
    enrollment_repository = EnrollmentRepository(db)
    user_repository = UserRepository(db)
    course_repository = CourseRepository(db)
    return EnrollmentService(enrollment_repository, user_repository, course_repository)
