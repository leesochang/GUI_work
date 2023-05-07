import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

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

#Creating three checkbuttons
chVarDis = tk.IntVar
check1 = tk.Checkbutton(win, text = "Disabled", variable=chVarDis, state = 'disabled')
check1.select()
check1.grid(column=0, row=4, stick = tk.W)

chVarUn = tk.IntVar
check2 = tk.Checkbutton(win, text = "UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, stick = tk.W)

chVarEn = tk.IntVar
check3 = tk.Checkbutton(win, text = "Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, stick = tk.W)

#radiobutton globals
colors = ["Blue", "Gold", "Red"]

def radCall():
    radSel = radVar.get()
    if radSel == 0: win.configure(background=colors[0])
    elif radSel == 1: win.configure(background=colors[1])
    elif radSel == 2: win.configure(background=colors[2])

radVar = tk.IntVar()

#selecting a non-existing index value for radVar
radVar.set(99)

for col in range(3):
    curRad = tk.Radiobutton(win, text = colors[col], variable=radVar, value = col, command = radCall)
    curRad.grid(column=col, row=5, sticky=tk.W)

#Using a scrolled Text control
scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(win, width = scrol_w, height = scrol_h, wrap=tk.WORD) #warp = tk.CHAR 모든 문자를 래핑
scr.grid(column=0, columnspan=3)


name_entered.focus()

win.mainloop()