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
more_samples = sample*5
print(tickets(more_samples))