import random

def winning_nums():
    l = []
    for i in range(0,7):
        x = random.randint(1,40)
        while(x in l):
            x = random.randint(1,40)
        l.append(x)
    return l