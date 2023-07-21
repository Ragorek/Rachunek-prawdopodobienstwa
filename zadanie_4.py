import pandas as pd
from matplotlib import pyplot
import random

throws = 7
dist = 0
ALL_SIMULATIONS = 1000000
all_sum = []
X = []
prob_of_sum = []
dystrybuant = []

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
    prob_of_sum.append(all_sum.count(i)/len(all_sum))
    X.append(i)
    dist += all_sum.count(i)/len(all_sum)
    dystrybuant.append(dist)
    print("xi : {}| pi : {}%".format(X[i-7],round(prob_of_sum[i-7]*100,4)))

input("Enter by kontynuować...")

df = pd.DataFrame({"Suma pol":X,"Prawdopodobienstwo":prob_of_sum})
df.plot(x="Suma pol", y="Prawdopodobienstwo", kind='scatter')	
pyplot.title("Gestosc")
pyplot.show()

df = pd.DataFrame({"Suma pol":X,"Prawdopodobienstwo":dystrybuant})
df.plot(x="Suma pol", y="Prawdopodobienstwo", kind='scatter')
pyplot.title("Dystrybuanta")
pyplot.show()