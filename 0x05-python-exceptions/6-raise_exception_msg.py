class NameError(Exception):
    def __init__(self, message=""):
        super().__init__(message)


def raise_exception_msg(message=""):
    raise NameError(message)
