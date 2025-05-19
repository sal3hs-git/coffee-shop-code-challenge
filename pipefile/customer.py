class Customer:
    def __init__(self, name):
        self.name = name  

    def name(self):
        return self._name

    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters.")
        self._name = value
