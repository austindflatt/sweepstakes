class Contestant:
    def __init__(self, first_name, last_name, email, registration_number):
        self.contestant = {first_name, last_name, email, registration_number}
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.registration_number = registration_number
    def is_winner(self):
        pass