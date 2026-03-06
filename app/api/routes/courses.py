from fastapi import APIRouter, Depends, status

from app.api.dependencies import get_course_service
from app.core.response import build_response
from app.schemas.course import CourseCreate, CourseOut, CourseUpdate
from app.services.course_service import CourseService

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.post("", status_code=status.HTTP_201_CREATED)
def create_course(payload: CourseCreate, service: CourseService = Depends(get_course_service)):
    course = service.create_course(payload)
    return build_response(True, "Course created successfully", CourseOut.model_validate(course).model_dump())


@router.get("")
def list_courses(service: CourseService = Depends(get_course_service)):
    courses = [CourseOut.model_validate(course).model_dump() for course in service.list_courses()]
    return build_response(True, "Courses retrieved successfully", courses)


@router.get("/{course_id}")
def get_course(course_id: int, service: CourseService = Depends(get_course_service)):
    course = service.get_course(course_id)
    return build_response(True, "Course retrieved successfully", CourseOut.model_validate(course).model_dump())


@router.put("/{course_id}")
def update_course(course_id: int, payload: CourseUpdate, service: CourseService = Depends(get_course_service)):
    course = service.update_course(course_id, payload)
    return build_response(True, "Course updated successfully", CourseOut.model_validate(course).model_dump())


@router.delete("/{course_id}")
def delete_course(course_id: int, service: CourseService = Depends(get_course_service)):
    service.delete_course(course_id)
    return build_response(True, "Course deleted successfully", None)
