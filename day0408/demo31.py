# 以下代码仅在Ubuntu执行
# fork方法不支持windows

import os
# print(os.cpu_count())
data = 1
print('main process id %d parent pid %d'%(os.getpid(), os.getppid()))
pid = os.fork()
# print(pid)
if pid == 0:
    print('child1 data',data)
    data = 2
    # print('child1 process %d parent pid %d'% (os.getpid(), os.getppid()))
    pid2 = os.fork()
    if pid2 == 0:
        print("child2",data)
        # print('child2 process %d parent pid %d'%(os.getpid(),os.getppid()))
    else:
        print("child1", data)
        print("child1 processid %d" % (os.getpid()))
else:
    data = 3
    print("main data",data)
    # print('main process %d'% os.getpid())

