# import queue
# import sys
from QueuedCharCount import QueuedCharCount
from QueuedFileRead import QueuedFileRead
from BlockingQueue import BlockingQueue

def main():
    file_queue = BlockingQueue("file!!", 50)
    text_queue = BlockingQueue("text!!", 50)
    looping = True
    count_dic = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }

    file_thread = QueuedFileRead(file_queue, text_queue)
    char_thread = QueuedCharCount(text_queue, count_dic)

    file_thread.start()
    char_thread.start()

    while looping:
        response = input("Enter a command -> read <file name>, print, and quit: ").replace('\n', '')
        response = response.strip().split()

        if 0 < len(response):
            if response[0] == "read":
                if 1 < len(response):
                    try:
                        file = open(response[1], 'r')
                        file_queue.enqueue(file)
                    except IOError:
                        print ("Could not read file:", response[1])
            elif response[0] == "print":
                for key, in sorted(count_dic):
                    print(key + ": " + str(count_dic.get(key)))
            elif response[0] == "quit":
                print("Due to multiple threads. please use ctrl+c to exit (ignore exception)")
                break
            else:
                print("Unknown command: " + str(response))

if __name__ == '__main__':
    main()