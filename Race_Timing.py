racenumber = 0
time = 0
while True:
    race = input("How long did it take to run?")
    if not race:
        break
    
    else:
        racenumber += 1
        time += float(race)
    
myaverage = time / racenumber 
print("Average of {0}, over {1} races".format(myaverage, racenumber))
