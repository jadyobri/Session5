#added for math operations
import math as m

#added because of numpy  ops
import numpy as np

#found on:https://stackoverflow.com/questions/61288473/why-python-cant-show-the-exact-value-of-sin-function
#used for more exact pi and sin operation
from sympy import sin, pi


#found from:https://towardsdatascience.com/how-to-easily-create-tables-in-python-2eaea447d8fd
#used for table(might change if needed)
from tabulate import tabulate

#print(type(float(sin(pi))))

#pi type is different than float, so I need it to be float
#linspace is used to generate 1000 values from 0 to 2pi in same increasing amount
v = float(2*pi)
man = np.linspace(0.0, v, num=1000)

#list made for sin opertions
#for loop used to append all the sin values
#if statements used to give the exact value for pi related numbers since pi is not exact here
san = []
for i in man:
    #san.append(i)
    if(i == v or i == v/2):
        san.append(0.0)
    elif(i == v/4):
        san.append(1.0)
    elif(i == v/(1*(1/3))):
        san.append(-1.0)
    else:
        san.append(float(sin(i)))

#new list as a list of lists for table
#appended the string of sin(x) and x for the top labeling
#for loop from 0 to 1000
#placehold used to take in a list of both the sin(x) and x for that index into the list
#placehold is added to the list as a list for the list of lists.
new = []
new.append(["sin(x)", "x"])
for x in range(0,1000):
    placehold = []
    placehold.append(san[x])
    placehold.append(man[x])
    new.append(placehold)


#prints the table
print(tabulate(new))