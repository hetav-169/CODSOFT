from tkinter import *
from tkinter import messagebox

def update_count():
    count_label.config(text="Total Tasks: " + str(task_list.size()))

def add_task():
    task = task_entry.get()

    if task != "":
        task_list.insert(END, task)
        task_entry.delete(0, END)
        update_count()
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def remove_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
        update_count()
    except:
        messagebox.showwarning("Warning", "Please select a task!")

def clear_tasks():
    if messagebox.askyesno("Clear All", "Do you want to remove all tasks?"):
        task_list.delete(0, END)
        update_count()

root = Tk()
root.title("To-Do List Application")
root.geometry("500x600")
root.resizable(False, False)
root.config(bg="lightblue")

title = Label(
    root,
    text="TO-DO LIST",
    font=("Arial", 22, "bold"),
    bg="lightblue",
    fg="darkblue"
)
title.pack(pady=15)

task_entry = Entry(
    root,
    width=30,
    font=("Arial", 14)
)
task_entry.pack(pady=10)

add_btn = Button(
    root,
    text="Add Task",
    width=15,
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=add_task
)
add_btn.pack(pady=5)
task_list = Listbox(
    root,
    width=40,
    height=15,
    font=("Arial", 12)
)
task_list.pack(pady=15)

count_label = Label(
    root,
    text="Total Tasks: 0",
    font=("Arial", 12, "bold"),
    bg="lightblue",
    fg="darkgreen"
)
count_label.pack()

remove_btn = Button(
    root,
    text="Remove Task",
    width=15,
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    command=remove_task
)
remove_btn.pack(pady=5)

clear_btn = Button(
    root,
    text="Clear All",
    width=15,
    font=("Arial", 12, "bold"),
    bg="orange",
    fg="white",
    command=clear_tasks
)
clear_btn.pack(pady=5)
footer = Label(
    root,
    text="Made by Mikey | Python Project",
    font=("Arial", 10),
    bg="lightblue",
    fg="gray"
)
footer.pack(side=BOTTOM, pady=10)

root.mainloop()
