from typing import List

from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database import Base


class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    workload: Mapped[int] = mapped_column(Integer, nullable=False)

    enrollments: Mapped[List["Enrollment"]] = relationship(back_populates="course", cascade="all, delete-orphan")
