import threading

class QueuedFileRead (threading.Thread):
    id = None
    name = None
    file_queue = None
    text_queue = None

    def __init__(self, file_queue, text_queue):
        super(QueuedFileRead, self).__init__()
        self.file_queue = file_queue
        self.text_queue = text_queue

    def run(self):
        while True:
            file = self.file_queue.dequeue()
            file_content = file.read()
            self.text_queue.enqueue(file_content)
