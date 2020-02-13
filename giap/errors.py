class GIAPError(Exception):
    def __init__(self, message):
        self.message = message


class ConsumerError(GIAPError):
    pass
