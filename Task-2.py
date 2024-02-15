def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.read().splitlines()
        return tasks
    except FileNotFoundError:
        return []

def add_task(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def delete_task(tasks):
    print("Current tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")
    index = int(input("Enter the number of the task you want to delete: ")) - 1
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task number!")

def view_tasks(tasks):
    print("Current tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n*** To-Do List App ***")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            delete_task(tasks)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
