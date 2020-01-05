# Make a y variable.
# Make a x variable.
# Change y and x based on random numbers.
# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.
import random
import operator
import matplotlib.pyplot
import agentframeworkIO
import csv

def distance_between(agents_row_a, agents_row_b):
    #distance between
    #print(str(agents_row_a))
    #print(str(agents_row_b))
    
    diff = ( ((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2) )**0.5
        
    return (str(diff))
    
#print ("Rand Industries")


#populating environment
environment = []
f = open('in.txt')
dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in dataset:
    envrow = []
    for value in row:
       envrow.append(value)
    environment.append(envrow)
f.close()
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

#Agent creation
num_of_agents = 10
cage = 99999

#Agent creating loop
#Random integers between 1 and 99 for first agents x and y coo-ordinates
agents = []
for i in range(num_of_agents):
    #agents.append([random.randint(1,99),random.randint(1,99)])
    agents.append(agentframeworkIO.Agent(environment))
    #print ("Agent "+str(i)+ ":- Start Coords Y:" + str(agents [i][0]) + " X:" + str(agents [i][1]))

#move agents
for j in range(cage):
    #control loop for agents movements
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()

             
#Print End Co-ordinates
for i in range(num_of_agents):
    print ("Agent "+str(i)+ ":- End Coords Y:" + str(agents[i].y) + " X:" + str(agents[i].y))



#distances between
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
print("The largest distance is: "+ str(max(distances)))
print("The smallest distance is: "+ str(min(distances)))
#print(distances)
#print(environment)

#graph output
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
painttype = ['chocolate','crimson','red','orange','yellow','palegreen','forestgreen','blue','violet','purple']
pt = 0
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y, color=painttype[pt])
    pt+=1
    
matplotlib.pyplot.show()

for i in range(num_of_agents):
    print(str(agents[i]))

#environment output
e = []
for row in environment:
    envrow = []
    for value in row:
       envrow.append(value)
    e.append(envrow)
with open('environmentfile.csv', mode='w') as envy:
    enwrite = csv.writer(envy, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for lines in e:
        enwrite.writerow(lines)


#file output
a = []
for i in range(num_of_agents):
	a.append("Agent "+ str(i) + " has eaten " +str(agents[i].store)+ "\n");
f = open("anotherfile.txt", 'a') #w puts the file into write mode
for row in a:
	f.write(row)
f.close()

#Can you get the agents to wander around the full environment by finding out the size of environment inside the agents, and using the size when you randomize their starting locations and deal with the boundary conditions? 