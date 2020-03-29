from tkinter import *
import math
root = Tk()
sirka = root.winfo_screenwidth()
vyska = root.winfo_screenheight()


root.attributes("-fullscreen",True)

angle_in_degrees = 264
uhol_minuty = 270
uhol_hodiny = 270
def sekunda():
    canvas.delete('all')
    global x
    global y
    global angle_in_degrees
    if angle_in_degrees == 360:
        angle_in_degrees = 0
    angle_in_degrees += 6
    angle_in_radians = angle_in_degrees * math.pi / 180
    line_length = 300
    x = 650 + line_length * math.cos(angle_in_radians)
    y = 375 + line_length * math.sin(angle_in_radians)

    canvas.create_text(650,500,text='R O L E X',font=('Roman',30))

    uhol = 270
    for i in range(12):
        uhol += 30
        canvas.create_text(650 + line_length * math.cos(uhol * math.pi / 180),
                           375 + line_length * math.sin(uhol * math.pi / 180),
                           text=i+1, font=('Purisa', 30))


    canvas.create_oval(300,40,1000,710,width = 15)
    canvas.create_line(650,375,x,y,width= 5,fill='red')

    global uhol_minuty
    if uhol_minuty == 360:
        uhol_minuty = 0
    uhol_minuty += 0.1
    angle_in_radians = uhol_minuty * math.pi / 180
    line_length = 300
    x1 = 650 + line_length * math.cos(angle_in_radians)
    y1 = 375 + line_length * math.sin(angle_in_radians)
    canvas.create_line(650, 375, x1, y1, width=15, fill='black')

    global uhol_hodiny
    if uhol_hodiny == 360:
        uhol_hodiny = 0
    uhol_hodiny += 0.00833333333
    angle_in_radians = uhol_hodiny * math.pi / 180
    line_length = 250
    x2 = 650 + line_length * math.cos(angle_in_radians)
    y2 = 375 + line_length * math.sin(angle_in_radians)
    canvas.create_line(650, 375, x2, y2, width=20, fill='blue')
    root.after(1000,sekunda)


canvas = Canvas(root, width = sirka, height = vyska)
canvas.place(x=-2,y=-2)

ex=Button(root,text='exit',command=root.destroy)
ex.place(x = 0,y = 0)

sekunda()

mainloop()
