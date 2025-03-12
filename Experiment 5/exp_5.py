tasks = []

def show_tasks():
    if not tasks:
        print("task is not found.")
    else:
        for i in tasks:
            print(i)

def add_task(name):
    tasks.append(name)
    print("Task is added", name)

def remove_task(name):
    if name in tasks:
        tasks.remove(name)
        print("Task is removed:", name)
    else:
        print("Task is not found.")

def sort_tasks():
    tasks.sort()
    print("Tasks is  sorted.")

while True:
    print("1. Show the Tasks")
    print("2. Add the Task")
    print("3. Remove the Task")
    print("4. Sort the Tasks")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        name = input("Enter the task: ")
        add_task(name)
    elif choice == '3':
        name = input("Enter the task to remove it: ")
        remove_task(name)
    elif choice == '4':
        sort_tasks()
    elif choice == '5':
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
    print()
