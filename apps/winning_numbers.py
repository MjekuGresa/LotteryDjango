import random

def winning_nums():
    l = []
    for i in range(0,7):
        x = random.randint(1,40)
        while(x in l):
            x = random.randint(1,40)
        l.append(x)
    return l

def winning_ticket(draw_numbers, tickets):
    list_count = []
    for ticket in tickets:
        count = 0
        for i in range(0, len(ticket)):
            if(int(ticket[i]) in draw_numbers):
                count = count + 1
        list_count.append(count)
    return list_count