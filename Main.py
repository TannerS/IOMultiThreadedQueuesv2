from BlockingQueue import BlockingQueue
from TestThread import TestThread
import time

def main():
    size = 200
    limit = 100
    queue = BlockingQueue(limit)

    thread = TestThread(queue, size)
    thread.start()

    for i in range (0, size):
        value = queue.dequeue()
        print("Dequeue: " + str(value))
        time.sleep(1)

if __name__ == '__main__':
    main()
