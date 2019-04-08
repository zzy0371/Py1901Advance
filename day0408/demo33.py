from multiprocessing import Process
import time
def processmain(pam1,pam2,**kwargs):
    print('++',pam1[0],pam2,kwargs)
    pam1.append(2)
    print(pam1)

def main():
    list1 = [1]
    p1 = Process(target=processmain,args=(list1,list1),kwargs={"name":'zzy'})
    p1.start()
    p1.join()
    print(list1)


if __name__ == "__main__":
    main()


"""
进程之间传参
一个进程修改不会影响其他进程数据
提供元组参数 args 字典参数kwargs 



"""