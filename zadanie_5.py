import random
from scipy.stats import shapiro

dist = 0
throws = 7
ALL_SIMULATIONS = 100000
all_sum = []
X = []
dystrybuant = []
all_means = []
all_sums_count = []
TRAILS = 100

def random_simulation(throws):
    move = []
    i = 0
    while(i<throws):
        move.append(random.randint(1,6))
        i+=1
    return move

for i in range(ALL_SIMULATIONS):
    simulation = random_simulation(throws)
    sum = 0
    for throw in simulation:
        sum += throw
    all_sum.append(sum)

for i in range(throws*1,throws*6+1):
    all_sums_count.append(all_sum.count(i))
    X.append(i)

for i in range(TRAILS):
    random_sums = random.sample(X,counts=all_sums_count,k=5)
    mean = 0
    for sum in random_sums:
        mean += sum/5
    all_means.append(mean)

print(shapiro(all_means))




