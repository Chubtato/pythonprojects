#!/usr/bin/python
#-----------------------------------------------------------------
# This program is a class of quadratics
# Author: Paurush
#
# Date : 2/4/2018
#
# Version : 1.1
#
# copyright (C)
#-----------------------------------------------------------------

class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def setA(self, a):
        self.a = a

    def setB(self, b):
        self.b = b

    def setC(self, c):
        self.c = c

    def getA(self):
        return(self.a)

    def getB(self):
        return(self.b)

    def getC(self):
        return(self.c)
    def doSolutionsExist(self):
        if (self.b*self.b - 4*self.a*self.c) < 0:
            return(False)
        else:
            return(True)
    def solutions(self):
        if(self.a==0):
            return("Not a Quadratic")
        elif(self.doSolutionsExist() == False):
            return("No Solution")
        else:
            solution1 = (-1*self.b + (self.b*self.b - 4*self.a*self.c)**0.5)/(2*self.a)
            solution2 = (-1*self.b - (self.b*self.b - 4*self.a*self.c)**0.5)/(2*self.a)

            return(solution1, solution2)

#
# Main program
#
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

top = Tk()
top.title("Quadratic Equation Solver")

frame = ttk.Frame(top)
frame.grid(row = 0, column = 0,sticky=(N, W, E, S))

def labelQuadratic(a,b,c):
    quad = Quadratic(int(str(a.get())),int(str(b.get())),int(str(c.get())))
    if (quad.a == 0):
        lab = ttk.Label(frame, text=quad.solutions()).grid(column=0,row=4,sticky=W)
    elif (quad.doSolutionsExist() == False):
        lab = ttk.Label(frame, text=quad.solutions(), background="red").grid(column=0,row=4,sticky=W)
    else:
        lab = ttk.Label(frame, text="Your Solution is: {0}".format(quad.solutions()), background="yellow").grid(column=0,row=4,sticky=W)

def tableCreate(a,b,c):
    table = {}
    for i in range(-21,20):
        table[i] = int(str(a.get()))*i*i+int(str(b.get()))*i+int(str(c.get()))

    return(table)
    
def clearValues():
    a_entry.delete(0,END)
    b_entry.delete(0,END)
    c_entry.delete(0,END)

a = StringVar()
b = StringVar()
c = StringVar()

a.set("")
c.set("")
b.set("")

ttk.Label(frame, text="a:").grid(column=0, row=0, sticky=W)
ttk.Label(frame, text="b:", foreground="blue").grid(column=0, row=1, sticky=W)
ttk.Label(frame, text="c:", foreground="red").grid(column=0, row=2, sticky=W)

a_entry = ttk.Entry(frame, width = 10,textvariable =a)
a_entry.grid(column = 1, row = 0, sticky=(W,E))

b_entry = ttk.Entry(frame, width = 10,textvariable =b)
b_entry.grid(column = 1, row = 1, sticky=(W,E))

c_entry = ttk.Entry(frame, width = 10,textvariable =c)
c_entry.grid(column = 1, row = 2, sticky=(W,E))

def plotFunction():
    graph = Tk()
    graph.title("Graph")

    canvas_width = 600
    canvas_height = 600
    w = Canvas(graph, width=canvas_width,height=canvas_height)
    
    def createGrid():
        distance = 10
        for i in range(0, int(canvas_height/distance)):
            w.create_line(0,distance*i, canvas_width, distance*i, fill="#D5DBDB")
        for i in range(0, int(canvas_width/distance)):
            w.create_line(distance*i, 0, distance*i, canvas_height, fill="#D5DBDB")
        for i in range(0,int(canvas_height/distance)):
            w.create_line(295,distance*2*i, 305, distance*2*i, fill = "#000000")
            w.create_line(distance*2*i, 295, distance*2*i,305, fill = "#000000")
        
        w.create_line(canvas_width/2, 0, canvas_width/2, canvas_height, fill="#000000")
        w.create_line(0,canvas_height/2, canvas_width, canvas_height/2, fill="#000000")

    createGrid()
    
    def motion(event):
        w.itemconfigure(tag,text="(%r,%r)"%(event.x-300,-1*(event.y-300)))

    tag = w.create_text(20,20,text="",anchor="nw")
    w.bind("<Motion>", motion)    
    graph.bind('<Motion>', motion)
    
    table = tableCreate(a,b,c)

    for key in table:
        w.create_oval(298+key,298-table[key],302+key,302-table[key], fill="red")
    for key in table:
        if key != 19:
            w.create_line(300+key,300-table[key],300+key+1, 300-table[key+1],fill="red")
    def clearGraph():
        w.delete(ALL)
        createGrid()
    w.pack()

    clear2 = ttk.Button(graph, text = "Clear",command = lambda: clearGraph())
    clear2.pack()

    graph.mainloop()

solve = ttk.Button(frame, text = "Solve",command = lambda: labelQuadratic(a,b,c))
solve.grid(row = 3, column = 0, sticky=(W,E))

leave = ttk.Button(frame, text = "Quit",command = lambda: quit())
leave.grid(row = 3, column = 1, sticky=(W,E))

clear = ttk.Button(frame, text = "Clear",command = lambda: clearValues())
clear.grid(row = 3, column = 2, sticky=(W,E))

plot = ttk.Button(frame, text = "Plot",command = lambda: plotFunction())
solve.grid(row = 3, column = 3, sticky=(W,E))


for child in frame.winfo_children(): child.grid_configure(padx=5,pady=5)
a_entry.focus()


top.mainloop()




        
        
