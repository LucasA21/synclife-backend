from dataclasses import dataclass


@dataclass
class CreateTagDto:
    user_id: str
    name: str