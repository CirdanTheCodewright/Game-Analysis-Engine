## Game Analysis Engine - a tool to model and visualize open world game progression
"""
Author: Daniel Lowcay - CirdanTheCodewright
"""
## main file provided all functionality, other files are set up to model each specific game

import numpy as np
import pandas as pd
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import threading
import time
import sys
from PIL import ImageTk, Image

button5 = []

def close():
    rootUI.destroy()
    sys.exit()

def CreateGUI():
    # Create the GUI
    root = Tk()
    root.title("Game Analysis Engine")
    root.geometry("2560x1440")
    root.configure(background='black')
    # make the window fullscreen
    root.attributes('-fullscreen', True)

    # create main figure
    fig = plt.figure(dpi=144, figsize=(10,10))
    fig.patch.set_facecolor('black')

    # create a 2D dataframe called 'difficulty' with 1000 rows and 1000 columns filled with zeros
    difficulty = pd.DataFrame(np.zeros((1000, 1000)))

    ax = fig.add_subplot(111)
    sns.color_palette("coolwarm", as_cmap=True)
    sns.heatmap(ax=ax, data=difficulty,cbar=False,xticklabels=False,yticklabels=False,center=0.5)
    plt.tight_layout()
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)

    # save the heatmap as a png file called 'heatmap.png'
    fig.savefig('heatmap.png')

    # create a tkinter canvas on root
    canvas = Canvas(master=root)
    canvas.place(relx=0.5, rely=0.5, relwidth=9/16, relheight=1, anchor='center')

    # display the saved image using PIL on the tkinter canvas
    img = ImageTk.PhotoImage(Image.open('heatmap.png'))
    panel = canvas.create_image(1440/2, 1440/2, image=img, anchor=CENTER)

    panel2 = Label(canvas, image = img)
    #panel2.place(relx=0.7, rely=0.7, anchor='center', relwidth=0.5, relheight=0.5)

    global button5
    button5 = ttk.Button(root, text="Exit", command=lambda: exit())

    # add a button to end the program and close the window at the bottom left of the tkinter window
    exitButton = Button(root, text="Exit", command=lambda: close())
    exitButton.place(relx=0.01, rely=0.99, relwidth=0.05, relheight=0.05, anchor='sw')
    # make exitButton have a blue background, larger font and white text
    exitButton.configure(background='blue', font=('Arial', 20), fg='white')
    # give exitButton rounded edges
    exitButton['relief'] = 'groove'

    return root, fig, canvas, ax, panel, panel2


rootUI = []
figure = []
mainCanvas = []
ax = []
panel = []
panel2 = []

# create a 2D pandas dataframe called 'difficulty' with 1000 rows and 1000 columns filled with numbers between 0 and 1
#difficulty = pd.DataFrame(numpy.random.rand(1000, 1000))

rootUI, figure, mainCanvas, ax, panel, panel2 = CreateGUI()
#mainCanvas, figure = SeabornHeatmapinTkinter(difficulty,rootUI)

def Main():
    for i in range(1000):
        # update the pandas dataframe with new random values
        #difficulty = pd.DataFrame(numpy.random.rand(1000, 1000))

        # create a 2D pandas dataframe called 'difficulty' with 1000 rows and 1000 columns gradient filled from 1 in the middle to 0 at the edges without using loops
        difficulty = pd.DataFrame(np.linspace(1,0,1000).reshape(1,1000))
        difficulty = difficulty.append(pd.DataFrame(np.linspace(0,1,1000).reshape(1,1000)))

        ax.cla()
        sns.heatmap(ax=ax, data=difficulty,cbar=False,xticklabels=False,yticklabels=False,center=0.5)
        figure.savefig('heatmap.png')

        # display the saved image using PIL on the tkinter canvas
        img = ImageTk.PhotoImage(Image.open('heatmap.png'))
        #panel.configure(image=img)
        #panel = mainCanvas.create_image(0, 0, image=img, anchor=NW)
        mainCanvas.itemconfig(panel, image=img)

        #panel2.configure(image=img)

        #panel = Label(mainCanvas, image = img)
        #panel.place(relx=0.5, rely=0.5, anchor='center')

        #mainCanvas.create_image(0, 0, image=img, anchor=NW)
        #mainCanvas.itemconfig(BGimage, image=img)

        label2 = Label(mainCanvas, text = "testing")
        label2.place(relx=0.3, rely=0.5, anchor='center')

        label3 = mainCanvas.create_text((300,300), text="testing")



        #rectangle = mainCanvas.create_rectangle(0, 0, 1000, 1000, fill="black")

        mainCanvas.create_line(0, 0, 1000, 1000, fill="red", width=5)
        # move rectangle above the label image
        #mainCanvas.tag_raise(rectangle)

        # place button5 at a random location on the tkinter window
        button5.place(relx=np.random.rand(), rely=np.random.rand(), relwidth=0.05, relheight=0.05, anchor='center')

        time.sleep(0.1)
        print(i)

# run Main() in its own thread so the tkinter window can update
MainLoop = threading.Thread(target=Main)
MainLoop.start()

# run the main tkinter window loop in its own thread so the rest of the program can continue to run
rootUI.mainloop()


