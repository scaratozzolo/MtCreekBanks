import tkinter as tk
from PIL import Image, ImageGrab, ImageTk
from datetime import datetime
import os

b1 = "up"
xold, yold = None, None
height = 200
width = 1000

def signature(type, number, date):

    if not os.path.exists('data/{}/{}-{}-{}'.format(type, date.month, date.day, date.year)):
        os.makedirs('data/{}/{}-{}-{}'.format(type, date.month, date.day, date.year))

    popup = tk.Tk()
    def submit(widget):
        x=popup.winfo_rootx()+widget.winfo_x()
        y=popup.winfo_rooty()+widget.winfo_y()
        x1=x+widget.winfo_width()
        y1=y+widget.winfo_height()
        savename = 'data/{}/{}-{}-{}/{}-{}-{}-{}'.format(type, date.month, date.day, date.year, type, number, date.hour, date.minute)
        ImageGrab.grab().crop((x,y,x1,y1)).save("{}.png".format(savename))
        popup.quit()
        popup.destroy()


    drawing_area = tk.Canvas(popup, height = height, width=width)
    drawing_area.pack()
    drawing_area.bind("<Motion>", motion)
    drawing_area.bind("<ButtonPress-1>", b1down)
    drawing_area.bind("<ButtonRelease-1>", b1up)
    submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(drawing_area))
    submitbutton.pack()
    popup.mainloop()
    return "finish"


def b1down(event):
    global b1
    b1 = "down"           # you only want to draw when the button is down
                          # because "Motion" events happen -all the time-

def b1up(event):
    global b1, xold, yold
    b1 = "up"
    xold = None           # reset the line when you let go of the button
    yold = None

def motion(event):
    if b1 == "down":
        global xold, yold
        if xold is not None and yold is not None:
            event.widget.create_line(xold,yold,event.x,event.y,smooth=tk.TRUE)
                          # here's where you draw it. smooth. neat.
        xold = event.x
        yold = event.y

def displaysig(type, date, number):
    root = tk.Toplevel()
    canvas = tk.Canvas(root, width = 1000, height = 200)
    canvas.grid(row=0, column=0)
    print("data/{}/{}-{}-{}/{}-{}-{}-{}.png".format(type, date.month, date.day, date.year, type, number, date.hour, date.minute))
    img = ImageTk.PhotoImage(Image.open("data/{}/{}-{}-{}/{}-{}-{}-{}.png".format(type, date.month, date.day, date.year, type, number, date.hour, date.minute)))
    canvas.create_image(20, 20, anchor=tk.NW, image=img)
    root.mainloop()

if __name__ == "__main__":
    # displaysig("bar", datetime(month=7, day=21, year=2018, hour=20, minute=26), "1")
    signature("bar", "1", datetime.now())
