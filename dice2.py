results = {1:0,2:0,3:0,4:0,5:0,6:0}
prob = {1:0,2:0,3:0,4:0,5:0,6:0}
amount = 0
def roll(count):
    for i in range(count):
            x = randint(1,6)
            results[x] = results[x]+1
from random import *
while True:
    ask = input("Would you like to roll a dice? YES, NO, or RESULTS: ")
    if(ask == "YES"):
        howMany = int(input("How many times do you want to roll?"))
        roll(howMany)
        amount+= howMany
        
        
    elif (ask == "NO"):
        print("Exiting Now")
        exit()
    elif (ask == "RESULTS"):
        for item in results:
            print("%d appears %d times"%(item,results[item]))
            print("%f probability"%(results[item]/amount))
                
    else:
        print("Invalid Input.")
        
