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
num_of_agents = 10

#Agent creating loop
#Random integers between 1 and 99 for first agents x and y coo-ordinates
for i in range(num_of_agents):
    agents.append([random.randint(1,99),random.randint(1,99)])
    print ("Agent "+str(i)+ ":- Start Coords Y:" + str(agents [i][0]) + " X:" + str(agents [i][1]))


for i in range(num_of_agents):
    #control loop for agents movements
    cage = 0
    while cage < 100:
        #first agents y random control number
        danny = random.random()
        #first agents x random control number
        dannx = random.random()
        if danny < 0.5:
            agents [i][0] += 1
        else:
            agents [i][0] -= 1
    
        if dannx > 0.5:
            agents [i][1] += 1
        else:
            agents [i][1] += 1
        
        #keep agents within the area torus style
        if  agents [i][0] < 0:
               agents [i][0] = 99
        if  agents [i][0] > 99:
               agents [i][0] = 0
        
        if  agents [i][1] < 0:
               agents [i][1] = 99
        if  agents [i][1] > 99:
               agents [i][1] = 0       
             
        cage+=1
        
    

#distance between
#answer = 0
#xdiff = (agents [0][1]-agents [1][1]) #**(x1-x2)
#ydiff = (agents [0][0]-agents [1][0]) #**(y1-y2)


for i in range(num_of_agents):
    print ("Agent "+str(i)+": - End Coords Y:" + str(agents [i][0]) + " X:" + str(agents [i][1]))

#print ("Xdiff: " + str(xdiff) + " Ydiff: " + (str(ydiff)))

#the square of the differences
#answerx = (xdiff**2)
#answery = (ydiff**2)


#maths has errors when zero value is present
#if (xdiff != 0):
#    if (ydiff != 0):
        #x and y are both not zero
#        print ("Xdiff2: " + str(answerx) + " Ydiff2: " + (str(answery)))
#        answer = math.sqrt(answerx+answery)
#    else:
        #x is not zero but y is zero
#        print ("Xdiff2: " + str(answerx) + " Ydiff2: 0")
#       answer = math.sqrt(answerx)
#else:
#    if (ydiff != 0):
        #x is zero and y is not zero
#        print ("Xdiff2: 0 Ydiff2: " + (str(answery)))
#        answer = math.sqrt(answery)
#    else:
        #both are zero
#        print ("Xdiff2: 0 Ydiff2: 0")
#        answer = 0

#print ("The distance between is: "+ str(answer))
#print (max(agents))
#print (max(agents, key=operator.itemgetter(1)))


#graph output
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
painttype = ['chocolate','crimson','red','orange','yellow','palegreen','forestgreen','blue','violet','purple']
pt = 0
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0], color=painttype[pt])
    pt+=1
    
matplotlib.pyplot.show()



