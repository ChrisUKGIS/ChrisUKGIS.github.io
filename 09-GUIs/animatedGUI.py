#import random   #not currently used
#import operator #not currently used



import agtfmewkanim #the agent class itself
import csv #used to read in the environment file
import sys
import matplotlib
import matplotlib.pyplot #used to plot the figure
import matplotlib.animation #used to animate the figure
import tkinter #GUI library

#the update function which defines what will happen each time the animation updates
def update(frame_number):
    
    #global call changes the scope of the hunger variable to global
    global hunger
    
    #clears the figure if anything was drawn to it
    fig.clear()
    #sets the axis of the plotted items to 99 on both X and Y
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.xlim(0, 99)
    #adds the environment variable, the contents of in.txt, to the figure
    matplotlib.pyplot.imshow(environment)

    #iterates through the agents and each agent, moves, eats, shares with those close to it
    #adds their x and y data ready to be shown
    for i in range(num_of_agents):
       
        agents[i].move()     
        #adds amount the current agent has stored to hunger to count how much has been eaten 
        hunger += agents[i].store    
        agents[i].eat()
        agents[i].callout(volume)
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        print("X:" +str(agents[i].x)+" Y:"+str(agents[i].y))

#count function to return a value to the frames argument for the matlib animation
#keeps going until either 500 iterations have been or hunger is over 50000
def count():
    
    appetite = 0
    while (appetite < 500) & (hunger<50000):
        yield appetite
        appetite = appetite + 1
    print("Thats enough for now")

#assigns count to the variable "wordup"
#The figure will show the results of the function update,
#at an interval of 1, once, using the variable wordup to determine the number of frames
#set to run via the GUI
def run():
    global canvas
    wordup = count()
    animation = matplotlib.animation.FuncAnimation(fig, update, repeat=False, frames=wordup)
    canvas.draw() #Found that xxx.plot() had been depreciated and that xxxx.plot() worked instead - had me confused for a while

#Tells matplotlib to use TkAgg - Tkinter argument? an approximation of the GUI style of TKinter
matplotlib.use('TkAgg')

agents = []
n = 1
#hunger counts how much the agents have eaten
hunger = 0

#take commands from command line in the order: agents, iterations, volume - distance that agents can share between
#currently num_of_iterations is ignored and this will run to the condition of count() based on hunger and appetite
print (str(sys.argv[1]+" "+ sys.argv[2] +" "+ sys.argv[3]))
num_of_agents = int(sys.argv[1])
num_of_iterations = int(sys.argv[2])
volume = int(sys.argv[3])


#sets the size of the window it appears in
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False) #not currently used - autoscales the output window

#populating environment - reads in from the "in.txt" file and 
#adds the contents row by row to environement
environment = []
f = open('in.txt')
dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in dataset:
    envrow = []
    for value in row:
      envrow.append(value)
    environment.append(envrow)
f.close()

# Make the agents. Iterates through the number of agents specified calling their initiation and adding to the agents list
for i in range(num_of_agents):
    agents.append(agtfmewkanim.Agent(environment,agents))


root = tkinter.Tk()
root.wm_title("Tunnel Progress - moving the earth")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Earth Moving", command=run)

tkinter.mainloop() 


















