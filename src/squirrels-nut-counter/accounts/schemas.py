from pydantic import  UUID4, FileUrl

from models import ORJSONModel


class Bank(ORJSONModel):
    """Bank model.

    Attributes
    ----------
    id : UUID4
        Bank ID.
    name : str
        Bank name.
    logo_url : FileUrl
        Bank logo URL.
    color : str
        Bank color.
    """
    id: UUID4
    name: str
    logo_url: FileUrl
    color: str

class Card(ORJSONModel):
    """Card model.

    Attributes
    ----------
    id : UUID4
        Card ID.
    card_number : str
        Card number.
    user_name : str
        Card user name.
    user_surname : str
        Card user surname.
    logo_url : FileUrl
        Card logo URL.
    color : str
        Card color.
    """
    id: UUID4
    card_number: str
    user_name: str
    user_surname: str
    logo_url: FileUrl
    color: str

class Account(ORJSONModel):
    """Account model.

    Attributes
    ----------
    id : UUID4
        Account ID.
    account_number : str
        Account number.
    bank : Bank
        Account's bank.
    cards : list[Card]
        Account's cards.
    balance : float
        Account's balance.
    """
    id: UUID4
    name: str
    bank: Bank
    cards: list[Card] = []
    balance: float = 0.0
