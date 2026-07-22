import random
import time
def race_run():
    """前進步數，兔子每往前兩次會倒退一次，總賽長100"""
    rabbit = []
    turtle = []
    rabbit_num = 0
    turtle_num = 0
    rabbit_stop = 0
    while rabbit_num < 100:
        if rabbit_stop == 2:
            rabbit_num -= random.randint(1,5)
            rabbit_stop = 0
        else:
            rabbit_num += random.randint(3,8)
            rabbit_num = min(100,rabbit_num)
            rabbit_stop += 1
        rabbit.append(rabbit_num)    

    while turtle_num < 100:
        turtle_num += random.randint(2,5)
        turtle_num = min(100,turtle_num)
        turtle.append(turtle_num)

    if len(rabbit) > len(turtle):
        win = "烏龜獲勝"
        for i in range(len(rabbit)-len(turtle)):
            turtle.append(100)
    else:
        win = "兔子獲勝"
        for i in range(len(turtle)-len(rabbit)):
            rabbit.append(100)
    return rabbit, turtle, win

def result(rabbit, turtle, win):
    print("Kyle:", "\t🐇","\nPobby:", "\t🐢")
    for i in range(len(rabbit)):
        time.sleep(0.5)
        print("\033[2A\033[K\rKyle:", f"\t{rabbit[i]*"."}", "🐇","\nPobby:", f"\t{turtle[i]*"."}", "🐢")
    print("\n", win)




