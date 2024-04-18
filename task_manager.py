import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack(pady=10)

        self.view_button = tk.Button(root, text="View Task", command=self.view_task)
        self.view_button.pack()

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.recommend_button = tk.Button(root, text="Recommend Task", command=self.recommend_task)
        self.recommend_button.pack()

        self.load_tasks()

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.write_task(task_text)
            self.tasks.append(task_text)
            self.task_listbox.insert(tk.END, task_text)
            self.task_entry.delete(0, tk.END)

    def view_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.task_listbox.get(selected_index)
            messagebox.showinfo("View Task", selected_task)

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.task_listbox.get(selected_index)
            updated_task_text = simpledialog.askstring("Update Task", "Enter updated task:", initialvalue=selected_task)
            if updated_task_text:
                self.tasks[selected_index[0]] = updated_task_text
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, updated_task_text)
                self.save_tasks()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.task_listbox.delete(selected_index)
            self.save_tasks()

    def recommend_task(self):
        if self.tasks:
            recommended_task = random.choice(self.tasks)
            messagebox.showinfo("Recommended Task", f"Recommended Task: {recommended_task}")
        else:
            messagebox.showinfo("Recommended Task", "No tasks available to recommend")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
                for task in self.tasks:
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def write_task(self, task):
        try:
            with open("tasks.txt", "a") as file:
                file.write(task + "\n")
        except IOError:
            messagebox.showerror("Error", "Unable to write task to file.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
