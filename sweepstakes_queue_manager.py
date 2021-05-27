from sweep_queue import Queue


class SweepstakeQueueManager:
    def __init__(self):
        self.queue = Queue()
        self.name = 'queue manager'

    def insert_sweepstakes(self, sweepstakes):
        self.queue.enqueue(sweepstakes)
        print(f"\nqueue: {self.queue.queue}")

    def get_sweepstakes(self):
        self.queue.dequeue()
        print(f"\nqueue: {self.queue.queue}")