class InvalidInputError(Exception):

    def __init__(self, message="Введені символи повинні бути літерами"):
        self.message = message
        super().__init__(self.message)
