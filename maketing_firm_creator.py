from marketing_firm import MarketingFirm
from sweepstakes_stack_manager import SweepstakesStackManager
from sweepstakes_queue_manager import SweepstakeQueueManager


class MarketingFirmCreator:
    @staticmethod
    def choose_manager_type():
        manager_type = [SweepstakeQueueManager(), SweepstakesStackManager()]
        manager_type_choice = input("\nManager type options:\n\t1: queue manager\n\t2: stack manager\nselection: ")

        if manager_type_choice == "1":
            manager_type = manager_type[0]
            print(f"manager type: {manager_type.name}")
        elif manager_type_choice == "2":
            manager_type = manager_type[1]
            print(f"manager type: {manager_type.name}")

        return MarketingFirm(manager_type)