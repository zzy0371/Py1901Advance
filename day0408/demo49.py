import threading

def myrun():
    print("++")
def thread1():
    print('--')


class MyThread(threading.Thread):
    def run(self):
        print('++')

if __name__ == "__main__":

    # t1 = threading.Thread(target=thread1)
    # print(t1.run)
    # t1.run = myrun
    # t1.start()

    t2 = MyThread()
    t2.start()


