from app.core.exceptions import NotFoundException
from app.entities.course import Course
from app.repositories.course_repository import CourseRepository
from app.schemas.course import CourseCreate, CourseUpdate


class CourseService:
    def __init__(self, repository: CourseRepository):
        self.repository = repository

    def create_course(self, payload: CourseCreate) -> Course:
        course = Course(
            title=payload.title,
            description=payload.description,
            workload=payload.workload,
        )
        return self.repository.create(course)

    def list_courses(self) -> list[Course]:
        return self.repository.get_all()

    def get_course(self, course_id: int) -> Course:
        course = self.repository.get_by_id(course_id)
        if not course:
            raise NotFoundException("Course not found")
        return course

    def update_course(self, course_id: int, payload: CourseUpdate) -> Course:
        course = self.get_course(course_id)
        course.title = payload.title
        course.description = payload.description
        course.workload = payload.workload
        return self.repository.update(course)

    def delete_course(self, course_id: int) -> None:
        course = self.get_course(course_id)
        self.repository.delete(course)
