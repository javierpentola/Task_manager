import tkinter as tk
from tkinter import messagebox
import requests

def add_task():
    title = entry_title.get()
    description = entry_description.get()
    status = entry_status.get()
    shift = entry_shift.get()
    assigned_to = entry_assigned_to.get()
    if title and description and status and shift and assigned_to:
        task = {
            'title': title,
            'description': description,
            'status': status,
            'shift': shift,
            'assigned_to': assigned_to
        }
        response = requests.post('http://127.0.0.1:5000/task', json=task)
        if response.status_code == 201:
            messagebox.showinfo("Success", "Task added successfully")
        else:
            messagebox.showerror("Error", "Failed to add task")
    else:
        messagebox.showwarning("Input error", "All fields are required")

app = tk.Tk()
app.title("Restaurant Task Manager")

tk.Label(app, text="Title").grid(row=0)
tk.Label(app, text="Description").grid(row=1)
tk.Label(app, text="Status").grid(row=2)
tk.Label(app, text="Shift").grid(row=3)
tk.Label(app, text="Assigned To").grid(row=4)

entry_title = tk.Entry(app)
entry_description = tk.Entry(app)
entry_status = tk.Entry(app)
entry_shift = tk.Entry(app)
entry_assigned_to = tk.Entry(app)

entry_title.grid(row=0, column=1)
entry_description.grid(row=1, column=1)
entry_status.grid(row=2, column=1)
entry_shift.grid(row=3, column=1)
entry_assigned_to.grid(row=4, column=1)

tk.Button(app, text="Add Task", command=add_task).grid(row=5, column=1)

app.mainloop()
