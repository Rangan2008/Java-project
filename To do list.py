from tkinter import *
import sqlite3
def add_task():
    task = field.get()
    if task != "":
        cursor.execute("INSERT INTO taskd(title) VALUES(?)", (task,))
        connect.commit()
        listbox.insert(END, task)
        field.delete(0, END)
        error_label.config(text="")
    else:
        error_label.config(text="Please enter a task")
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        selected_task = listbox.get(selected_task_index)
        cursor.execute("DELETE FROM taskd WHERE title=?", (selected_task,))
        connect.commit()
        listbox.delete(selected_task_index)
        error_label.config(text="")
    except IndexError:
        error_label.config(text="Please select a task to delete")
def delete_all_tasks():
    cursor.execute("DELETE FROM taskd")
    connect.commit()
    listbox.delete(0, END)
    error_label.config(text="All tasks deleted")
def exit_app():
    connect.close()
    raj.destroy()
raj = Tk()
raj.title("Things to do list")
raj.geometry("650x490+550+250")
raj.resizable(100,100)
raj.configure(bg="red")
connect = sqlite3.connect('practice.db')
cursor = connect.cursor()
cursor.execute("create table if not exists taskd(title text)")
task_label = Label(
    text="TO-DO-LIST",
    font=("Times", 14, "bold"),
    background="Yellow",
    foreground="Black"
)
task_label.grid(row=0, column=0, columnspan=2, pady=10)
task_label = Label(
    text="Enter \n the Task Title:",
    font=("Arial", 14, "bold"),
    background="Yellow",
    foreground="Black"
)
task_label.grid(row=1, column=0, sticky='nw', padx=20, pady=10)
field = Entry(
    font=("Arial", 14,"bold"),
    width=35,
    foreground="black",
    background="white"
)
field.grid(row=1, column=1, padx=20, pady=10, sticky='w')
add_button = Button(
    text="Add Task",
    font=("Arial", 12,"bold"),
    width=10,
    background="Yellow",
    foreground="Black",
    command=add_task
)
add_button.grid(row=2, column=0, padx=20, pady=10, sticky='e')
delete_button = Button(
    text="Delete Task",
    font=("Arial", 12,"bold"),
    width=10,
    background="Yellow",
    foreground="Black",
    command=delete_task
)
delete_button.grid(row=2, column=1, padx=20, pady=10, sticky='w')
delete_all_button = Button(
    text="Delete All",
    font=("Arial", 12,"bold"),
    width=10,
    background="Yellow",
    foreground="Black",
    command=delete_all_tasks
)
delete_all_button.grid(row=3, column=0, padx=20, pady=10, sticky='e')
exit_button = Button(
    text="Exit",
    font=("Arial", 12,"bold"),
    width=10,
    background="Yellow",
    foreground="Black",
    command=exit_app
)
exit_button.grid(row=3, column=1, padx=20, pady=10, sticky='w')
listbox = Listbox(
    font=("Arial", 14),
    width=50,
    height=10,
    background="white",
    foreground="black"
)
listbox.grid(row=4, column=0, columnspan=2, padx=20, pady=10)
cursor.execute("SELECT title FROM taskd")
rows = cursor.fetchall()
for row in rows:
    listbox.insert(END, row[0])
error_label = Label(
    text="",
    font=("Arial", 12, "bold"),
    background="red",
    foreground="yellow"
)
error_label.grid(row=5, column=0, columnspan=2)
raj.mainloop()
connect.close()
