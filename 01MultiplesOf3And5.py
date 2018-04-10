multiplesOf3=0
multiplesOf5=0
multiplesOf15=0
for i in range(1000):
    if (i%3==0):
        multiplesOf3+=i
    elif (i%5==0):
        multiplesOf5+=i
    elif (i%15==0):
        multiplesOf15+=i
total=multiplesOf3+multiplesOf5-multiplesOf15
print (total)