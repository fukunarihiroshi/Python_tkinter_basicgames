from random import *
a = randint(1,6)
a = "*"*3 + "A" + "*"*3



print(a)

pos = 0
iteration = 0
while True:
    iteration += 1
    input("iteration :"+str(iteration))
    pos = pos + randint(1,6)
    a = "*"*(pos-1) + "A" + "*"*(80-pos)
    print(a)

    if (pos>80):
        print("Goal!!", 80/iteration)
        break



