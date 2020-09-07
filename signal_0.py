"""
    信号方法处理僵尸
"""

import os
import signal

# 处理子进程退出,防止僵尸进程产生
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

pid = os.fork()

if pid < 0:
    pass
elif pid == 0:
    print("child PID:",os.getpid())
else:
    while True:
        pass
