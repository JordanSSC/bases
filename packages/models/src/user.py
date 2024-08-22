from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    id: int
    email: str
    firstName: str
    lastName: str