import tkinter as tk
import json, os
from tkinter import font as f

class Text:
    addButton = "Add"

def GetDb():
    if os.path.isfile('tasks.json'):
        return json.load(open("tasks.json", "r" ))
    else:
        return []

def SaveDb(data): 
    json.dump(data, open( "tasks.json", "w" ) )

def AppendToDb(task):
    data = GetDb()
    data.append(task)
    SaveDb(data)

window = tk.Tk()
window.configure(bg="white")
window.title("TO-DO App")
width = int(window.winfo_screenwidth() / 3)
height = int(window.winfo_screenheight() / 3)
window.geometry(f"{width}x{height}")
window.resizable(0, 0)


heading = tk.Label(window, text='Tasks',width=int(width/11) , bg="light gray")
input_info_label = tk.Label(window,text="Enter your task here...",width=int(width/15),bg="white")
label_font = f.Font(family='Arial', size=15)


list_tasks = tk.Listbox(window,justify="center",width=int(width/15),height=int(height/34),bd=0)
new_task_input = tk.Entry(window, justify="center", width=int(width/15),bg="white")

def reset_db(Event=None):
    SaveDb([])
    reset_task_list()

def reset_task_list():
    list_tasks.delete(0,"end")

clear_tasks = tk.Button(window,justify="center",text="Clear Tasks")


def add_item(Event=None):
    target = new_task_input.get()
    if target == "":
        return
    print(target)
    AppendToDb(target)
    list_tasks.insert("end",target)
    clear_input()

for el in GetDb():
    list_tasks.insert("end",el)

def clear_input(Event=None):
    new_task_input.delete(0,"end")

new_task_input.bind("<Return>", add_item)
new_task_input.bind("<Button-1>", clear_input)
clear_tasks.bind("<Button-1>", reset_db)


heading["font"]=label_font
new_task_input["font"] = label_font
list_tasks["font"] = label_font
input_info_label["font"] = label_font


clear_tasks.grid(row=0,column=1)
heading.grid(row=0, column=0, columnspan=2)
input_info_label.grid(row=1, column=0, columnspan=2)
new_task_input.grid(row=2, column=0, columnspan=2)
list_tasks.grid(row=3, column=0, rowspan=10, columnspan=2,pady=10)



if __name__ == '__main__':
    window.mainloop()  