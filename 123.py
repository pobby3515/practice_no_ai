import time
a = [2,100,60]
for b in a:
    time.sleep(2)
    print(f"\033[K{b*"."}",end="\r")