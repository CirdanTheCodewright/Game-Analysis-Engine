## Game Analysis Engine - a tool to model and visualize open world game progression
"""
Author: Daniel Lowcay - CirdanTheCodewright
"""
## main file provided all functionality, other files are set up to model each specific game

import numpy
import pandas as pd
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import threading
import time
import sys

def CreateGUI():
    # Create the GUI
    root = Tk()
    root.title("Game Analysis Engine")
    root.geometry("2560x1440")
    root.configure(background='black')
    # make the window fullscreen
    root.attributes('-fullscreen', True)

    # create main figure
    fig = plt.figure()
    fig.patch.set_facecolor('black')

    ax = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(relx=0.5, rely=0.5, relwidth=9/16, relheight=1, anchor='center')
    canvas.draw()

    difficulty = pd.DataFrame(numpy.random.rand(1000, 1000))
    sns.heatmap(ax=ax, data=difficulty, cmap="YlGnBu",cbar=False,xticklabels=False,yticklabels=False)

    plt.tight_layout()

    # add a button to end the program and close the window at the bottom left of the tkinter window
    exitButton = Button(root, text="Exit", command=lambda: exit())
    exitButton.place(relx=0.01, rely=0.99, relwidth=0.05, relheight=0.05, anchor='sw')
    # make exitButton have a blue background, larger font and white text
    exitButton.configure(background='blue', font=('Arial', 20), fg='white')
    # give exitButton rounded edges
    exitButton['relief'] = 'groove'

    return root, fig, canvas, ax

rootUI = []
figure = []
mainCanvas = []
ax = []

# create a 2D pandas dataframe called 'difficulty' with 1000 rows and 1000 columns filled with numbers between 0 and 1
difficulty = pd.DataFrame(numpy.random.rand(1000, 1000))

rootUI, figure, mainCanvas, ax = CreateGUI()
#mainCanvas, figure = SeabornHeatmapinTkinter(difficulty,rootUI)

def Main():
    for i in range(1000):
        # update the pandas dataframe with new random values
        difficulty = pd.DataFrame(numpy.random.rand(1000, 1000))

        ax.cla()
        sns.heatmap(ax=ax, data=difficulty, cmap="YlGnBu",cbar=False,xticklabels=False,yticklabels=False)
        mainCanvas.draw()
        

        time.sleep(0.1)
        print(i)

# run Main() in its own thread so the tkinter window can update
MainLoop = threading.Thread(target=Main)
MainLoop.start()

# run the main tkinter window loop in its own thread so the rest of the program can continue to run
rootUI.mainloop()


