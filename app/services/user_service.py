from app.core.exceptions import ConflictException, NotFoundException
from app.entities.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, payload: UserCreate) -> User:
        existing_user = self.repository.get_by_email(payload.email)
        if existing_user:
            raise ConflictException("Email already registered")

        user = User(name=payload.name, email=payload.email)
        return self.repository.create(user)

    def list_users(self) -> list[User]:
        return self.repository.get_all()

    def get_user(self, user_id: int) -> User:
        user = self.repository.get_by_id(user_id)
        if not user:
            raise NotFoundException("User not found")
        return user

    def update_user(self, user_id: int, payload: UserUpdate) -> User:
        user = self.get_user(user_id)
        user_with_same_email = self.repository.get_by_email(payload.email)

        if user_with_same_email and user_with_same_email.id != user_id:
            raise ConflictException("Email already registered")

        user.name = payload.name
        user.email = payload.email
        return self.repository.update(user)

    def delete_user(self, user_id: int) -> None:
        user = self.get_user(user_id)
        self.repository.delete(user)

    def get_user_courses(self, user_id: int) -> User:
        user = self.repository.get_with_courses(user_id)
        if not user:
            raise NotFoundException("User not found")
        return user
