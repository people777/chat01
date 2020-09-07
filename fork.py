"""
    fork函数演示
"""

import os
from time import sleep

pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    sleep(5)
    print("The new process")
else:
    sleep(4)
    print("The old process")

print("Fork test over")
