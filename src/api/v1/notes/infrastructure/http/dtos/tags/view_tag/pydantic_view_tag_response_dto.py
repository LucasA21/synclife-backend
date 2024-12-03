from pydantic import BaseModel
from src.api.v1.notes.infrastructure.persistence.models.sqlmodel_tags_model import (
    SqlModelTagsModel,
)


class PydanticViewTagsResponseDto(BaseModel):
    tag: SqlModelTagsModel