from enum import Enum


class Method(Enum):
    POST = "post"
    PUT = "put"


class Operation(str, Enum):
    INCREASE = "increase"
    APPEND = "append"
    REMOVE = "remove"
