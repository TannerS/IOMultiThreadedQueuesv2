import threading

class QueuedCharCount (threading.Thread):
    id = None
    name = None
    text_queue = None
    count_dic = None

    def __init__(self, text_queue, count_dic):
        super(QueuedCharCount, self).__init__()
        self.text_queue = text_queue
        self.count_dic = count_dic

    def run(self):
        while True:
            queue_str = self.text_queue.dequeue()
            for letter in queue_str:
                if (letter != ' ') and (letter != '\n'):
                    self.count_dic[letter] += 1
