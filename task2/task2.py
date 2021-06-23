from tkinter import *
import math as m

#створення вікна
window=Tk()
window.title("olya`s calculator <3")
window.geometry('470x330')

#створення поля вводу
box=Entry(window, width=150,bg='#edd4f0',fg="#fbfbfb",font=("Cambria Math",20))
box.place(x=10,y=10,height=50,width=400)

#створення кнопок
buttons=['=','1','2','3','+','-','C',
         '4','5','6','*','/','DEL',
         '7','8','9','cos','sin','%',
         '0','ln','log','ctg','tan','bin']
x=410
y=10
for i in buttons:
    a=lambda z=i: fun(z)
    Button(text=i,bg='#d3a6d8',fg="#f2f2f2",font=("Cambria Math",20),command=a).place(x=x,y=y,height=50,width=50)
    x+=80
    if x>450:
        x=10
        y+=60

#опис команд кнопок
def fun(buttn):
    if buttn=='=':
        box.insert(END,'=' + str(eval(box.get())))
    elif buttn=='cos':
        box.insert(END,'=' + str(m.cos(int(box.get()))))
    elif buttn=='sin':
        box.insert(END,'=' + str(m.sin(int(box.get()))))
    elif buttn=='tan':
        box.insert(END,'=' + str(m.tan(int(box.get()))))
    elif buttn=='ctg':
        box.insert(END,'=' + str(m.ctg(int(box.get()))))
    elif buttn=='log':
        box.insert(END,'=' + str(m.log(int(box.get()))))
    elif buttn=='ln':
        box.insert(END,'=' + str(m.log10(int(box.get()))))
    elif buttn=='C':
        box.delete(0,END)
    elif buttn=='DEL':
         box.delete(len(str(box.get()))-1)
    elif buttn == "bin":
        box.insert(END, '=' + str(bin(int(box.get()))))
    else:
        if '=' in box.get():
            box.delete(0,END)
        box.insert(END,buttn)
        window.mainloop()
            
