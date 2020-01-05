# Make a y variable.
# Make a x variable.
# Change y and x based on random numbers.
# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.
import random
import math
import operator
import matplotlib.pyplot

print ("Rand Industries")

agents = []

#Agent 1
#Random integers between 1 and 99 for first agents x and y coo-ordinates
agents.append([random.randint(1,99),random.randint(1,99)])

#Agent 2
#Random integers between 1 and 99 for second agents x and y coo-ordinates
agents.append([random.randint(1,99),random.randint(1,99)])

print ("Agent 1 - Start Coords Y:" + str(agents [0][0]) + " X:" + str(agents [0][1]))
print ("Agent 2 - Start Coords Y:" + str(agents [1][0]) + " X:" + str(agents [1][1]))

#loop count
cage = 0

#control loop for first agents movements

while cage < 3:
    #first agents y random control number
    danny = random.random()
    #first agents x random control number
    dannx = random.random()
    if danny < 0.5:
        agents [0][0] += 1
    else:
        agents [0][0] -= 1
    
    if dannx > 0.5:
        agents [0][1] += 1
    else:
        agents [0][1] += 1
    cage+=1
    


#loop count
cage = 0

#control loop for second agents movements

while cage < 3:
    #first agents y random control number
    danny = random.random()
    #first agents x random control number
    dannx = random.random()
    if danny < 0.5:
        agents [1][0] += 1
    else:
        agents [1][0] -= 1
    
    if dannx > 0.5:
        agents [1][1] += 1
    else:
        agents [1][1] -= 1
    cage+=1    

#distance between
answer = 0
xdiff = (agents [0][1]-agents [1][1]) #**(x1-x2)
ydiff = (agents [0][0]-agents [1][0]) #**(y1-y2)

print ("Agent 1 - End Coords Y:" + str(agents [0][0]) + " X:" + str(agents [0][1]))
print ("Agent 2 - End Coords Y:" + str(agents [1][0]) + " X:" + str(agents [1][1]))
print ("Xdiff: " + str(xdiff) + " Ydiff: " + (str(ydiff)))

#the square of the differences
answerx = (xdiff**2)
answery = (ydiff**2)


#maths has errors when zero value is present
if (xdiff != 0):
    if (ydiff != 0):
        #x and y are both not zero
        print ("Xdiff2: " + str(answerx) + " Ydiff2: " + (str(answery)))
        answer = math.sqrt(answerx+answery)
    else:
        #x is not zero but y is zero
        print ("Xdiff2: " + str(answerx) + " Ydiff2: 0")
        answer = math.sqrt(answerx)
else:
    if (ydiff != 0):
        #x is zero and y is not zero
        print ("Xdiff2: 0 Ydiff2: " + (str(answery)))
        answer = math.sqrt(answery)
    else:
        #both are zero
        print ("Xdiff2: 0 Ydiff2: 0")
        answer = 0

print ("The distance between is: "+ str(answer))
print (max(agents))
print (max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0], color='blue')
matplotlib.pyplot.scatter(agents[1][1],agents[1][0], color='red')
matplotlib.pyplot.show()



