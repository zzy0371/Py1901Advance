from multiprocessing import Process


def mainprocess():
    print('自定义入口函数')

class MyProcess(Process):
    def __init__(self):
        Process.__init__(self)
    def run(self):
        print('执行了')
def main():
    p1 = MyProcess()
    p1.start()

if __name__ == "__main__":
    main()

"""
当调用进程对象的start方法会执行进程的run方法 run方法相当于入口函数
如果在进程子类重写run方法  进程的target实例指定的入口函数废弃
"""

"""
Process类封装
Process传参

"""