from fastapi import APIRouter, Depends, status

from app.api.dependencies import get_user_service
from app.core.response import build_response
from app.schemas.user import UserCreate, UserOut, UserUpdate
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("", status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, service: UserService = Depends(get_user_service)):
    user = service.create_user(payload)
    return build_response(True, "User created successfully", UserOut.model_validate(user).model_dump())


@router.get("")
def list_users(service: UserService = Depends(get_user_service)):
    users = [UserOut.model_validate(user).model_dump() for user in service.list_users()]
    return build_response(True, "Users retrieved successfully", users)


@router.get("/{user_id}")
def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    user = service.get_user(user_id)
    return build_response(True, "User retrieved successfully", UserOut.model_validate(user).model_dump())


@router.put("/{user_id}")
def update_user(user_id: int, payload: UserUpdate, service: UserService = Depends(get_user_service)):
    user = service.update_user(user_id, payload)
    return build_response(True, "User updated successfully", UserOut.model_validate(user).model_dump())


@router.delete("/{user_id}")
def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    service.delete_user(user_id)
    return build_response(True, "User deleted successfully", None)


@router.get("/{user_id}/courses")
def get_user_courses(user_id: int, service: UserService = Depends(get_user_service)):
    user = service.get_user_courses(user_id)
    courses = [
        {
            "id": enrollment.course.id,
            "title": enrollment.course.title,
            "description": enrollment.course.description,
            "workload": enrollment.course.workload,
        }
        for enrollment in user.enrollments
    ]
    return build_response(
        True,
        "User courses retrieved successfully",
        {
            "user": UserOut.model_validate(user).model_dump(),
            "courses": courses,
        },
    )
