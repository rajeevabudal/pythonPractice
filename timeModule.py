import time

print(time.time())

t = time.localtime()

print(time.strftime("%Y-%m-%d %H:%M:%S", t))