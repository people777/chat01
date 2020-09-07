import os
from time import sleep

print("-------------")
a = 1
list01 = [1,2,3,4]
pid = os.fork()

if pid < 0:
    print("error")
elif pid == 0:
    print("child process")
    print("a = %d"%a)
    a = 100
    list01[0] = 15
else:
    sleep(2)
    print("parent process")
    print("a = %d" % a)
    print(list01)

print(a)


"""
    fork特点：pid = os.fork()
    1. 子进程会复制父进程全部内存空间，从fork下一句开始执行
    2. 父子进程各自独立运行，运行顺利不一定
    3. 利用父子进程fork返回值的区别，配合if结构让父子进程执行不同的内容几乎是固定搭配
    4. 父子进程有各自特有特征比如PID PCB命令集等
    5. 父进程fork之前开辟的空间子进程同样拥有，父子进程对各自空间的操作不会相互影响
    
"""