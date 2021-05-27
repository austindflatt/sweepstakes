from contestant import Contestant
from maketing_firm_creator import MarketingFirmCreator


def sweepstakes_start():
    market_firm = MarketingFirmCreator.choose_manager_type()

    sweepstake_1 = market_firm.create_sweepstakes()
    sweepstake_2 = market_firm.create_sweepstakes()
    sweepstake_3 = market_firm.create_sweepstakes()

    market_firm.manager.insert_sweepstakes(sweepstake_1.name)
    market_firm.manager.insert_sweepstakes(sweepstake_2.name)
    market_firm.manager.insert_sweepstakes(sweepstake_3.name)

    contestant_1 = Contestant()
    contestant_2 = Contestant()

    sweepstake_1.register_contestant(contestant_1)
    sweepstake_1.register_contestant(contestant_2)

    sweepstake_1.print_contestant_info(contestant_1)
    sweepstake_1.print_contestant_info(contestant_2)

    sweepstake_1.print_contestant_list()

    sweepstake_1.pick_winner()

    market_firm.manager.get_sweepstakes()
