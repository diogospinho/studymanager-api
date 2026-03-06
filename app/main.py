from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

from app.api.routes import courses, enrollments, users
from app.core.config import settings
from app.core.exceptions import AppException
from app.core.response import build_response
from app.entities import course, enrollment, user  # noqa: F401
from app.infrastructure.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(enrollments.router)


@app.exception_handler(AppException)
async def app_exception_handler(_: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content=build_response(False, exc.message, None),
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content=build_response(False, "Validation error", exc.errors()),
    )


@app.exception_handler(IntegrityError)
async def integrity_exception_handler(_: Request, __: IntegrityError):
    return JSONResponse(
        status_code=409,
        content=build_response(False, "Database integrity error", None),
    )


@app.get("/")
def health_check():
    return build_response(True, "StudyManager API is running", {"version": "1.0.0"})
