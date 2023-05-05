import tkinter as tk
from tkinter import ttk

win = tk.Tk()  #Tk 클래스의 인스턴스를 생성
win.title("Python GUI")  #제목 설정

#Add a Label
ttk.Label(win, text = "A Label").grid(column = 0, row = 0)

win.mainloop()