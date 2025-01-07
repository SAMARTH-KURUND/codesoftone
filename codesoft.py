# Define the Todo List class
class TodoList:
    def __init__(self):
        self.tasks = []

    # Add a new task to the list
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to your to-do list.")

    # Remove a task from the list
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from your to-do list.")
        else:
            print(f"Task '{task}' not found in your to-do list.")

    # Show all tasks
    def show_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("Your To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

# Function to run the To-Do List app
def todo_app():
    todo = TodoList()

    while True:
        print("\n=== To-Do List ===")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            task = input("Enter the task to add: ")
            todo.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo.remove_task(task)
        elif choice == '3':
            todo.show_tasks()
        elif choice == '4':
            print("Exiting the to-do list app. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid option (1-4).")

# Run the to-do list application
todo_app()
