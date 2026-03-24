# To-Do List Application (CLI)

tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            status = "✓" if tasks[i]["done"] else "✗"
            print(f"{i+1}. {tasks[i]['task']} [{status}]")

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task_name = input("Enter task: ")
        tasks.append({"task": task_name, "done": False})
        print("Task added successfully!")

    elif choice == 2:
        show_tasks()

    elif choice == 3:
        show_tasks()
        task_no = int(input("Enter task number to mark as done: "))
        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]["done"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number!")

    elif choice == 4:
        show_tasks()
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            tasks.pop(task_no - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number!")

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
