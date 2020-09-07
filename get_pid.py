import os

pid = os.fork()

if pid < 0:
    print("error")
elif pid == 0:
    print("child pid:",os.getpid())
    print("get parent pid",os.getppid())
else:
    print("pid = ",pid)
    print("parent pid",os.getpid())

