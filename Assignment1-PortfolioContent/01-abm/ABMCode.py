# Make a y variable.
# Make a x variable.
# Change y and x based on random numbers.
# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.
import random
import math

print ("Rand Industries")


#Agent 1
#Random integers between 1 and 99 for first agents x and y coo-ordinates
y1 = random.randint(1,99)
x1 = random.randint(1,99)

#Agent 2
#Random integers between 1 and 99 for second agents x and y coo-ordinates
y2 = random.randint(1,99)
x2 = random.randint(1,99)


print ("Agent 1 - Start Coords Y:" + str(y1) + " X:" + str(x1))
print ("Agent 2 - Start Coords Y:" + str(y2) + " X:" + str(x2))

#loop count
cage = 0

#control loop for first agents movements

while cage < 3:
    #first agents y random control number
    danny = random.random()
    #first agents x random control number
    dannx = random.random()
    if danny < 0.5:
        y1+=1
    else:
        y1-=1
    
    if dannx > 0.5:
        x1+=1
    else:
        x1-=1
    cage+=1
    


#loop count
cage = 0

#control loop for first agents movements

while cage < 3:
    #first agents y random control number
    danny = random.random()
    #first agents x random control number
    dannx = random.random()
    if danny < 0.5:
        y2+=1
    else:
        y2-=1
    
    if dannx > 0.5:
        x2+=1
    else:
        x2-=1
    cage+=1    

#distance between
answer = 0
xdiff = (x1-x2) #**(x1-x2)
ydiff = (y1-y2) #**(y1-y2)

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


print ("Agent 1 - End Coords Y:" + str(y1) + " X:" + str(x1))
print ("Agent 2 - End Coords Y:" + str(y2) + " X:" + str(x2))
print ("The distance between is: "+ str(answer))




