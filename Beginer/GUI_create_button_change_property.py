import tkinter as tk
from tkinter import ttk

win = tk.Tk()  #Tk 클래스의 인스턴스를 생성
win.title("Python GUI")  #제목 설정

#Add a Label
a_label = ttk.Label(win, text = "A Label")
a_label.grid(column=0, row=0)

#button Click Event Function
def click_me():
    action.configure(text="** I have been Clicked! **")
    a_label.configure(foreground='red')
    a_label.configure(text='A Red Label')

# Adding a Button
action = ttk.Button(win, text = "Click me!", command = click_me)
action.grid(column=1, row =0)


win.mainloop()