# Make a y variable.
# Make a x variable.
# Change y and x based on random numbers.
# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.
import random
import operator
import matplotlib.pyplot
import agentframework

def distance_between(agents_row_a, agents_row_b):
    #distance between
    #print(str(agents_row_a))
    #print(str(agents_row_b))
    
    diff = ( ((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2) )**0.5
        
    return (str(diff))
    
#print ("Rand Industries")

agents = []
num_of_agents = 10
cage = 100
jam = agentframework.Agent()
print(jam.x)
print(jam.y)
jam.move()
print(jam.x)
print(jam.y)

#Agent creating loop
#Random integers between 1 and 99 for first agents x and y coo-ordinates
for i in range(num_of_agents):
    #agents.append([random.randint(1,99),random.randint(1,99)])
    agents.append(agentframework.Agent())
    #print ("Agent "+str(i)+ ":- Start Coords Y:" + str(agents [i][0]) + " X:" + str(agents [i][1]))

#move agents
for j in range(cage):
    #control loop for agents movements
    for i in range(num_of_agents):
        agents[i].move()

             
#Print End Co-ordinates
for i in range(num_of_agents):
    print ("Agent "+str(i)+ ":- End Coords Y:" + str(agents[i].y) + " X:" + str(agents[i].y))

distances = []


i = 0
t = 1
while i < num_of_agents:
    while t < num_of_agents:
        distance = distance_between(agents[i],agents[t])       
        print ("The distance between Agents "+str(i)+" and "+str(t)+" is: "+ str(distance))
        distances.append(distance)
        #print(t)
        t += 1
    #print(i)
    i +=1
    t = i+1


#graph output
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
painttype = ['chocolate','crimson','red','orange','yellow','palegreen','forestgreen','blue','violet','purple']
pt = 0
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y, color=painttype[pt])
    pt+=1
    
matplotlib.pyplot.show()

print("The largest distance is: "+ str(max(distances)))
print("The smallest distance is: "+ str(min(distances)))
