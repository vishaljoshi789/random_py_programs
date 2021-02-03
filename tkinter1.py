from tkinter import *
root = Tk()
root.title("Ludo by Vishal")
root.geometry(("600x600"))
shape = Canvas(root, width = 700, height = 1000)
shape.pack()

# blue
shape.create_rectangle(0, 0, 200, 200,fill= "blue", outline = "black",width = 4)
b1 = shape.create_oval(30, 30, 80, 80, fill= "blue", outline= "black", width = 2)
b2 = shape.create_oval(110, 30, 160, 80, fill= "blue", outline= "black", width = 2)
b3 = shape.create_oval(30, 120, 80, 170, fill= "blue", outline= "black", width = 2)
b4 = shape.create_oval(110, 120, 160, 170, fill= "blue", outline= "black", width = 2)

# red
shape.create_rectangle(400, 0, 600, 200,fill= "red", outline = "black",width = 4)
r1 = shape.create_oval(430, 30, 480, 80, fill= "red", outline= "black", width = 2)
r2 = shape.create_oval(510, 30, 560, 80, fill= "red", outline= "black", width = 2)
r3 = shape.create_oval(430, 120, 480, 170, fill= "red", outline= "black", width = 2)
r4 = shape.create_oval(510, 120, 560, 170, fill= "red", outline= "black", width = 2)

# yellow
shape.create_rectangle(0, 400, 200, 600,fill= "yellow", outline = "black",width = 4)
y1 = shape.create_oval(30, 430, 80, 480, fill= "yellow", outline= "black", width = 2)
y2 = shape.create_oval(110, 430, 160, 480, fill= "yellow", outline= "black", width = 2)
y3 = shape.create_oval(30, 520, 80, 570, fill= "yellow", outline= "black", width = 2)
y4 = shape.create_oval(110, 520, 160, 570, fill= "yellow", outline= "black", width = 2)

# green
shape.create_rectangle(400, 400, 600, 600,fill= "green", outline = "black",width = 4)
g1 = shape.create_oval(430, 430, 480, 480, fill= "green", outline= "black", width = 2)
g2 = shape.create_oval(510, 430, 560, 480, fill= "green", outline= "black", width = 2)
g3 = shape.create_oval(430, 520, 480, 570, fill= "green", outline= "black", width = 2)
g4 = shape.create_oval(510, 520, 560, 570, fill= "green", outline= "black", width = 2)

# path
shape.create_line(0, 0, 600, 0, fill = "black", width = 5)
shape.create_line(0, 0, 0, 600, fill = "black", width = 5)
shape.create_line(0, 600, 600, 600, fill = "black", width = 5)
shape.create_line(600, 0, 600, 600, fill = "black", width = 5)
shape.create_line(332, 0, 332, 200, fill = "black", width = 3)
shape.create_line(266, 0, 266, 200, fill = "black", width = 3)
shape.create_line(0, 266, 200, 266, fill = "black", width = 3)
shape.create_line(0, 332, 200, 332, fill = "black", width = 3)
shape.create_line(266, 400, 266, 600, fill = "black", width = 3)
shape.create_line(332, 400, 332, 600, fill = "black", width = 3)
shape.create_line(400, 266, 600, 266, fill = "black", width = 3)
shape.create_line(400, 332, 600, 332, fill = "black", width = 3)
shape.create_line(200, 33, 400, 33, fill = "black", width = 3)
shape.create_line(200, 66, 400, 66, fill = "black", width = 3)
shape.create_line(200, 99, 400, 99, fill = "black", width = 3)
shape.create_line(200, 132, 400, 132, fill = "black", width = 3)
shape.create_line(200, 165, 400, 165, fill = "black", width = 3)
shape.create_rectangle(200, 200, 400, 400, fill = "silver", width = 3)






root.mainloop()