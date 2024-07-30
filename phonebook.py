class Phonebook:
    def __init__(self):
        self.contacts = {}

    def add(self, name, number):
        self.contacts[name] = number

    def lookup(self, name):
        return self.contacts[name]
