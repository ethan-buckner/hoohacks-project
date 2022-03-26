
from random import random
import numpy as np
from matplotlib import pyplot as plt

customers = 0

p = input("What probability of new customer? ")
p = float(p)
q = input("What is the probability of the first customer leaving? ")
q = float(q)

forward = p*(1-q)
backwards = q*(1-p)
same = (p*q)+((1-q)*(1-p))

time = input("How many minutes to run? ")
time = int(time)
totaltime= time

positions = [customers]

while time > 1:
    prob = random()
    if 0 < prob <= forward:
        customers += 1
    elif forward < prob <= (forward + same):
        customers = customers
    elif (forward + same) < prob <= 1:
        customers -= 1
    if customers == -1:
        customers = 0
    print(prob)
    print(customers)
    time -= 1
    positions.append(customers)

print("After " + str(totaltime) + " minutes, there are currently " + str(customers) + " customers.")

x = np.arange(0, totaltime)
plt.title("Customers in line at a given minute")
plt.xlabel("Time")
plt.ylabel("Customers")
plt.plot(x, positions, 'r-')
plt.show()



