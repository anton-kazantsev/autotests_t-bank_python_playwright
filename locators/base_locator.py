from typing import NamedTuple, Optional

class BaseLocator(NamedTuple):
    selector: str
    description: str
    nth: Optional[int] = None
    click: bool = None
    input: bool = None