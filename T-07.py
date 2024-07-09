class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for index, task in enumerate(self.tasks):
                status = "Done" if task["completed"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            print(f"Deleted task: {deleted_task['task']}")
        else:
            print("Invalid task number.")

def main():
    to_do_list = ToDoList()
    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ").strip()
        
        if choice == '1':
            task = input("Enter the task: ").strip()
            to_do_list.add_task(task)
            print(f"Task '{task}' added to the to-do list.")
        
        elif choice == '2':
            print("To-Do List:")
            to_do_list.view_tasks()
        
        elif choice == '3':
            task_number = int(input("Enter the task number to mark as completed: "))
            to_do_list.mark_task_completed(task_number)
        
        elif choice == '4':
            task_number = int(input("Enter the task number to delete: "))
            to_do_list.delete_task(task_number)
        
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
