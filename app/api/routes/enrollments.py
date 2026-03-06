from fastapi import APIRouter, Depends, status

from app.api.dependencies import get_enrollment_service
from app.core.response import build_response
from app.schemas.enrollment import EnrollmentCreate, EnrollmentOut
from app.services.enrollment_service import EnrollmentService

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])


@router.post("", status_code=status.HTTP_201_CREATED)
def create_enrollment(payload: EnrollmentCreate, service: EnrollmentService = Depends(get_enrollment_service)):
    enrollment = service.create_enrollment(payload)
    return build_response(
        True,
        "Enrollment created successfully",
        EnrollmentOut.model_validate(enrollment).model_dump(),
    )
