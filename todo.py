import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        # Title Label
        self.label = tk.Label(root, text="To-Do List", font=("Arial", 16, "bold"))
        self.label.pack(pady=10)

        # Listbox for tasks
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.mark_done_button = tk.Button(root, text="Mark as Done", command=self.mark_done)
        self.mark_done_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack(pady=5)

    def add_task(self):
        """Ask the user for task input and add it to the list"""
        n_tasks = simpledialog.askinteger("Number of Tasks", "How many tasks do you want to add?")
        
        if n_tasks:
            for _ in range(n_tasks):
                task = simpledialog.askstring("Task Input", "Enter the task:")
                if task:
                    self.tasks.append({"task": task, "done": False})
                    self.task_listbox.insert(tk.END, f"{task} - Not Done")

    def mark_done(self):
        """Mark selected task as done"""
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["done"] = True
            self.task_listbox.delete(index)
            self.task_listbox.insert(index, f"{self.tasks[index]['task']} - Done")
            messagebox.showinfo("Success", "Task marked as done!")
        else:
            messagebox.showwarning("Warning", "Select a task to mark as done.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
