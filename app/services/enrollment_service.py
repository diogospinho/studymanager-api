from app.core.exceptions import ConflictException
from app.entities.enrollment import Enrollment
from app.repositories.course_repository import CourseRepository
from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.user_repository import UserRepository
from app.schemas.enrollment import EnrollmentCreate


class EnrollmentService:
    def __init__(
        self,
        enrollment_repository: EnrollmentRepository,
        user_repository: UserRepository,
        course_repository: CourseRepository,
    ):
        self.enrollment_repository = enrollment_repository
        self.user_repository = user_repository
        self.course_repository = course_repository

    def create_enrollment(self, payload: EnrollmentCreate) -> Enrollment:
        user = self.user_repository.get_by_id(payload.user_id)
        if not user:
            from app.core.exceptions import NotFoundException
            raise NotFoundException("User not found")

        course = self.course_repository.get_by_id(payload.course_id)
        if not course:
            from app.core.exceptions import NotFoundException
            raise NotFoundException("Course not found")

        enrollment = self.enrollment_repository.get_by_user_and_course(payload.user_id, payload.course_id)
        if enrollment:
            raise ConflictException("Enrollment already exists for this user and course")

        new_enrollment = Enrollment(user_id=payload.user_id, course_id=payload.course_id)
        return self.enrollment_repository.create(new_enrollment)
