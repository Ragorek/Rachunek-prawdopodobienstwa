import random
THROWS = 7
Suma = 0
Suma2 = 0
Won_moves = []
ALL_SYMULATIONS = 100000

def random_simulation(throws):
    move = []
    i = 0
    while(i<throws):
        move.append(random.randint(1,6))
        i+=1
    return move


for i in range(ALL_SYMULATIONS):
    simulation = random_simulation(THROWS)
    pos = 0
    pos_num = 0
    station1 = False
    station2 = False
    station3 = False
    station4 = False
    for move in simulation:
        pos += move
        if(pos == 5):
            station1 = True
        elif(pos == 15):
            station2 = True
        elif(pos == 25):
            if(station1):
                Won_moves.append(pos_num)
            station3 = True
        elif(pos == 35):
            if(station2 and not(station1 and station3)):
                Won_moves.append(pos_num)
            station4 = True
        pos_num += 1
    if((station1 and station3) or (station2 and station4)):
        Suma += 1
        if(simulation[0] == 3):
            Suma2 +=1

Won_moves = {1:Won_moves.count(0),2:Won_moves.count(1),3:Won_moves.count(2),4:Won_moves.count(3),5:Won_moves.count(4),6:Won_moves.count(5),7:Won_moves.count(6)}

print("\nzadanie 1\n")
print("Prawdopodobieństwo zdarzenia: {:.4f}%".format(Suma/ALL_SYMULATIONS*100))
input("Enter by kontynuować...")
print("\nzadanie 2\n")
print("Prawdopodobieństwo Zdarzenia warunkowego: {:.4f}%".format(Suma2/ALL_SYMULATIONS*100))
input("Enter by kontynuować...")
print("\nZadanie 3\n")
for x in Won_moves:
    print("Ruch {} : {}".format(x,Won_moves.get(x)))
