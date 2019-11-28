# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 23:14:21 2019

@author: GISWork
"""

import tkinter
import requests

def run():
    run()

def runhouse():
    print("This is runs house")
    pass

def bush():
    print(xandy)

# Just showing menu elements
root = tkinter.Tk()

page = requests.get('https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html', verify=False)
xandy = page.text

c = tkinter.Canvas(root, width=200, height=200)
c.pack() # Layout
c.create_rectangle(0, 0, 200, 200, fill="blue")

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
model_menu.add_command(label="Run DMC", command=runhouse)
model_menu.add_command(label="Run running up that hill", command=bush)

model_menu.entryconfig("Run model", state="disabled")
# Until the user has chosen files, then:
#model_menu.entryconfig("Run model", state="normal") 

tkinter.mainloop() # Wait for interactions. 