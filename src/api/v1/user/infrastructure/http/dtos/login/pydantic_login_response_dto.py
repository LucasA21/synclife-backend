from pydantic import BaseModel
from src.api.v1.user.infrastructure.persistence.models import SqlModelUserModel


class PydanticLoginResponseDto(BaseModel):
    user: SqlModelUserModel
    session_token: str