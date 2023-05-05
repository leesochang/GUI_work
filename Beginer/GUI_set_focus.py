import tkinter as tk
from tkinter import ttk

win = tk.Tk()  #Tk 클래스의 인스턴스를 생성
win.title("Python GUI")  #제목 설정

#Add a Label
a_label = ttk.Label(win, text = "A Label")
a_label.grid(column=0, row=0)

#button Click Event Function
def click_me():
    action.configure(text="Hello  " + name.get())

#Changing our Label
ttk.Label(win, text = "Enter a name:").grid(column=0, row=0)

#Adding a Text box Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width =12, textvariable = name)
name_entered.grid(column=0, row=1)


# Adding a Button
action = ttk.Button(win, text = "Click me!", command = click_me)
action.grid(column=1, row =1)

name_entered.focus()

win.mainloop()