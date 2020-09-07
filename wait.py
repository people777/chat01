import os

pid = os.fork()

if pid < 0:
    print("error")
elif pid == 0:
    print("child process",os.getpid())
    os._exit(2)
else:
    # pid,status = os.wait() # 等待处理僵尸
    pid,status = os.waitpid(-1,os.WNOHANG)
    print("pid",pid)
    print("status",status)
    while True:
        pass