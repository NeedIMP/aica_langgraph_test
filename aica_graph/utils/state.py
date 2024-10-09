from typing import TypedDict

class AicaGraphState(TypedDict, total=False):
    from_user: str
    to_user: str
    cc: str
    bcc: str
    messageBody: str
    isCorrespondenceBetweenUsersBool: bool
    isAicaInCopyBool: bool
    aica_action_terminal_message: str


