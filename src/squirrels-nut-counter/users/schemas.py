from pydantic import UUID4, FileUrl

from accounts.schemas import Account

from models import ORJSONModel

class User(ORJSONModel):
    """User model.

    Attributes
    ----------
    id : UUID4
        User ID.
    name : str
        User name.
    surname : str
        User surname.
    avatar_url : FileUrl
        User avatar URL.
    accounts : list[Account]
        User's accounts.
    """
    id: UUID4
    name: str
    surname: str
    avatar_url: FileUrl
    accounts: list[Account] = []
