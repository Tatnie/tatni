from tkinter import *
root = Tk()

button1=Button(master=root, text='druk hier')
button1.pack( pady=50,side=LEFT)

button2=Button(master=root, text='druk hier')
button2.pack( pady=50,side=RIGHT)

button3=Button(master=root, text='druk hier')
button3.pack( side=TOP,pady=50)

root.mainloop()

