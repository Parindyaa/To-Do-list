class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, time_frame=None):
        self.tasks.append({"task": task, "time_frame": time_frame, "done": False})

    def list_tasks(self):
        for idx, task in enumerate(self.tasks, 1):
            status = "✓" if task["done"] else "✗"
            time_info = f" (Time: {task['time_frame']})" if task["time_frame"] else ""
            print(f"{idx}. {task['task']}{time_info} - {status}")

    def mark_done(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1]["done"] = True

    def show_summary(self):
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task["done"])
        print(f"Total Tasks: {total_tasks}, Completed: {completed_tasks}")

    def calculate_productivity(self):
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task["done"])
        productivity = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        print(f"Productivity: {productivity:.2f}%")

if __name__ == "__main__":
    todo = ToDoList()
    todo.add_task("Complete assignment", "2 hours")
    todo.add_task("Review cybersecurity notes")
    todo.list_tasks()
    todo.mark_done(1)
    todo.show_summary()
    todo.calculate_productivity()
