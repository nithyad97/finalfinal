from tkinter import *


a = int(input("Enter your value of X1: "))
b = int(input("Enter your value of Y1: "))

c = int(input("Enter your value of X2: "))
d = int(input("Enter your value of Y2: "))

g = int(input("Enter your value of X3: "))
h = int(input("Enter your value of Y3: "))

e = int(input("Enter your value of X4: "))
f = int(input("Enter your value of Y4: "))



i = ((a+75)+(c-25))/2
j = ((b+50)+ (d+50))/2
k = (c-25)+((e-25-c+25))/3
l = (d+50)+ ((f-50-d-50))/3
i1 = (c-25)+((e-25-c+25)*2)/3
j1 = (d+50)+ ((f-50-d-50)*2)/3
m = (e-25+g+75)/2
n = (f-50+h-50)/2
o = (g+75+(a+75 -g-75)/3) 
p = (h-50+(b+50-h+50)/3)
q = (g+75+((a+75 -g-75)*2)/3) 
r = (h-50+((b+50-h+50)*2)/3)

my_window = Tk()
my_canvas = Canvas(my_window,width=400,height=400,background='white')
my_canvas.grid(row=0,column=0)
my_canvas.create_line(a,b,c+50,d,width=5)
my_canvas.create_line(c+50,d,e+50,f,width=5)
my_canvas.create_line(e+50,f,g,h,width=5)
my_canvas.create_line(g,h,a,b,width=5)

my_canvas.grid(row=0,column=0)
my_canvas.create_line(i,j,i1,j1,width=1)
my_canvas.create_line(o,p,i1,j1,width=1)
my_canvas.create_line(o,p,i,j,width=1)
my_canvas.create_line(m,n,k,l,width=1)
my_canvas.create_line(m,n,q,r,width=1)
my_canvas.create_line(q,r,k,l,width=1)

my_window.mainloop()
