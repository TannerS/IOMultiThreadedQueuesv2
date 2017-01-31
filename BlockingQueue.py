# https://docs.python.org/3/library/asyncio-sync.html
from threading import Lock, Semaphore

class BlockingQueue:
    queue = None
    mutex = None
    empty = None
    full = None

    def __init__(self, max = 100):
        self.queue = []
        self.empty = Semaphore(value=max)
        self.full = Semaphore(0)
        self.mutex = Lock()

    def enqueue(self, data):
        self.empty.acquire(blocking=True)
        self.mutex.acquire(blocking=True)
        self.queue.append(data)
        self.mutex.release()
        self.full.release()

    def dequeue(self):
        self.full.acquire(blocking=True)
        self.mutex.acquire(blocking=True)
        item = self.queue.pop(0)
        self.mutex.release()
        self.empty.release()
        return item




