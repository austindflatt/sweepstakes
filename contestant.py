import random


class Contestant:
    def __init__(self):
        self.first_name = str
        self.last_name = str
        self.email_address = str
        self.registration_number = int

        self.first_name = input("\nFirst Name: ")
        self.last_name = input("Last Name: ")
        self.email_address = input("Email Address: ")
        rand = random.Random(1, 100)
        self.registration_number = rand
        print(
            f"contestant info:\n\tfirst name: {self.first_name}\n\tlast name: {self.last_name}\n\temail address: {self.email_address}\n\tregistration number: {self.registration_number}")

    def notify(self, is_winner):
        print(f"Congratulations {is_winner.first_name} {is_winner.last_name}!")
