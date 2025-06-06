import json
import os

# File to store tasks
FILENAME = "tasks.json"
tasks = []

# Load tasks from file
def load_tasks():
    global tasks
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            tasks = json.load(file)
    else:
        tasks = []

# Save tasks to file
def save_tasks():
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    save_tasks()
    print("Task added.")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i, t in enumerate(tasks):
            status = "✓" if t["done"] else "✗"
            print(f"{i+1}. {t['task']} [{status}]")

def complete_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark complete: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True
            save_tasks()
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            removed = tasks.pop(num)
            save_tasks()
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
load_tasks()  # Load saved tasks first

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Tasks saved. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
