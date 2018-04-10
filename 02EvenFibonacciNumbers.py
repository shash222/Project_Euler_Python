x=1
y=2
z=x+y
total=0;
if (x%2==0):
    total+=2
elif (y%2==0):
    total+=2
elif (z%2==0):
    total+=2
while(z<4000000):
    x=y
    y=z
    z=x+y
    if (z%2==0):
        total+=z
print (total)