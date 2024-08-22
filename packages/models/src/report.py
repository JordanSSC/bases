from dataclasses import dataclass
from datetime import date

from packages.models.src.user import User


@dataclass(frozen=True)
class Report:
    id: int
    creationDate: date
    user: User