import threading

class TestThread (threading.Thread):
    queue = None
    max = None

    def __init__(self, queue, max):
        super(TestThread, self).__init__()
        self.max = max
        self.queue = queue

    def run(self):
        for i in range(0, self.max):
            self.queue.enqueue(i + 1)
            print("Enqueue: " + str(i + 1))



