tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

def remove_task():
    task_number = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_number < len(tasks):
        removed_task = tasks.pop(task_number)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task number.")

def show_menu():
    print("To-Do List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")