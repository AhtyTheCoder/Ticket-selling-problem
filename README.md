# Ticket-selling-problem
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.  Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.  Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?  Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.

import numpy as np
def tickets(people):
    balance = []
    index = 0
    if people[0] == 50 or people[0] == 100:
        return "NO"
    while index < len(people):
        if people[index] == 100:
            if sum(balance) >= 75:
                if 50 in balance:
                    del balance[-1]
                    del balance[0]
                else:
                    del balance[0]
                    del balance[0]
                    del balance[0]
            else:
                return "NO"
        elif people[index] == 100:
            continue
        else:
            balance.append(people[index])
            balance.sort()
            if people[index] == 50:
                if balance[0] == 25:
                    del balance[0]
                else:
                    return "NO"
        index += 1
    return 'YES'

sample = list(np.random.choice([25, 50, 100], 10, p=[0.55, 0.3, 0.15]))
print(tickets(sample))

print(sample)
