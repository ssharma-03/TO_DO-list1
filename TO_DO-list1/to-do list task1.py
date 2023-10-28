import tkinter as tk
from tkinter import messagebox

def Create_task():
    title = entry_title.get()
    description = entry_description.get()
    if title:
        task_list.insert(tk.END, f"{title} - {description}")
        entry_title.delete(0, tk.END)
        entry_description.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a title for the task.")

def Delete_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)

app = tk.Tk()
app.title("To-Do List")

frame = tk.Frame(app)
frame.pack(pady=10)

label_title = tk.Label(frame, text="Title:")
label_title.grid(row=0, column=0, padx=5)
entry_title = tk.Entry(frame)
entry_title.grid(row=0, column=1, padx=5)

label_description = tk.Label(frame, text="Add Description:")
label_description.grid(row=1, column=0, padx=5)
entry_description = tk.Entry(frame)
entry_description.grid(row=1, column=1, padx=5)

add_button = tk.Button(frame, text="Add Task", command=Create_task)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

remove_button = tk.Button(frame, text="Remove Task", command=Delete_task)
remove_button.grid(row=3, column=0, columnspan=2)

task_list = tk.Listbox(app, selectmode=tk.SINGLE)
task_list.pack(padx=20, pady=20)

app.mainloop()
