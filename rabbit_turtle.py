import random
from tqdm import tqdm
from time import sleep
import time
import os

rabbit = []
turtle = []
rabbit_keep = True
turtle_keep = True
rabbit_num = 0
turtle_num = 0
rabbit_stop = 0
while rabbit_keep:
    if rabbit_stop == 2:
        rabbit_num -= random.randint(1,5)
        rabbit_stop = 0
    else:
        rabbit_num += random.randint(3,8)
        rabbit_num = min(100,rabbit_num)
        rabbit_stop += 1
    if rabbit_num >= 100:
        rabbit_keep = False
    rabbit.append(rabbit_num)    

while turtle_keep:
    turtle_num += random.randint(2,5)
    turtle_num = min(100,turtle_num)
    if turtle_num >= 100:
        turtle_keep = False
    turtle.append(turtle_num)



if len(rabbit) > len(turtle):
    twin = "烏龜獲勝"
    for i in range(len(rabbit)-len(turtle)):
        turtle.append(100)
else:
    rwin = "兔子獲勝"
    for i in range(len(turtle)-len(rabbit)):
        rabbit.append(100)

print("Kyle:", "\t🐇","\nPobby:", "\t🐢")
a=0
b=0
for _ in range(len(rabbit)):
    time.sleep(0.5)
    print("\033[2A\033[K\rKyle:", f"\t{rabbit[a]*"."}", "🐇","\nPobby:", f"\t{turtle[b]*"."}", "🐢")
    a += 1
    b += 1
if twin is None:
    print(rwin)
else:
    print(twin)