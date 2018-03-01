from tkinter import *

root = Tk()

def leftClick(event):
    print("Left")


def rightClick(event):
    print("Right")
    
 #adjusts size of window in screen. invisbile frame. needs widget to bind events to.   
frame = Frame(root, width = 300, height = 250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-1>", rightClick)
frame.pack()


root.mainloop()
