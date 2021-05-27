class Sweepstake:
    def __init__(self):
        self.name = input("\nwhat is the name of this sweepstake?: ")
        self.contestant_list = []

    def register_contestant(self, contestant):
        contestant_dictionary = {"first name": contestant.first_name,
                                 "last name": contestant.last_name,
                                 "email": contestant.email_address,
                                 "registration number": contestant.registration_number}

        self.contestant_list.append(contestant_dictionary)

    def pick_winner(self):
        rand = random.randrange(0, len(self.contestant_list))
        winner = self.contestant_list[rand]
        print(f"\nSweepstake winner: {winner['first name']} {winner['last name']}")

    def print_contestant_info(self, contestant):
        print(
            f"\ncontestant info:\n\tfirst name: {contestant.first_name}\n\tlast name: {contestant.last_name}\n\temail: {contestant.email_address}\n\tregistration number: {contestant.registration_number}")

    def print_contestant_list(self):
        print(f"\nContestants in {self.name} sweepstake:\n\t{self.contestant_list}")

    def notify_contestants(self, message):
        for contestant in self.contestant_list:
            contestant.notify(message)