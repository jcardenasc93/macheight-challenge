class BaseError(BaseException):
    """ Base exception class """
    pass

class InvalidInputError(BaseError):
    def __init__(self):
        super().__init__("Invalid input received")

class InvalidInputValuesError(BaseError):
    def __init__(self):
        super().__init__("Check input values. Some of them are not integers")

class MatchingPairsNotFound(BaseError):
    def __init__(self):
        super().__init__("Matching pairs not found for given values")
