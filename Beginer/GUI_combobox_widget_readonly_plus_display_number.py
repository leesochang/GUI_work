import tkinter as tk
from tkinter import ttk

win = tk.Tk()  #Tk 클래스의 인스턴스를 생성
win.title("Python GUI")  #제목 설정

#Add a Label
a_label = ttk.Label(win, text = "A Label")
a_label.grid(column=0, row=0)

#button Click Event Function
def click_me():
    action.configure(text="Hello  " + name.get()+ ' '+number_chosen.get())

#Changing our Label
ttk.Label(win, text = "Enter a name:").grid(column=0, row=0)

#Adding a Text box Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width =12, textvariable = name)
name_entered.grid(column=0, row=1)


# Adding a Button
action = ttk.Button(win, text = "Click me!", command = click_me)
action.grid(column=2, row =1)

ttk.Label(win, text="Choose a number: ").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state = 'readonly')
number_chosen['values'] = list(range(1, 13))
number_chosen.grid(column=1, row=1)  # <= Combobox in column 1
number_chosen.current(0)

name_entered.focus()

win.mainloop()