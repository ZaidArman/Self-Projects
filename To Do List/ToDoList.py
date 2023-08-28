def main():
    tasks = []
    
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. List Tasks")
        print("4. Remove Completed Tasks")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter task: ")
            tasks.append({'task': task, 'completed': False})
            print("Task added successfully.")
        elif choice == '2':
            list_tasks(tasks)
            task_index = int(input("Enter the index of the task to mark as completed: "))
            if task_index < len(tasks):
                tasks[task_index]['completed'] = True
                print("Task marked as completed.")
            else:
                print("Invalid task index.")
        elif choice == '3':
            list_tasks(tasks)
        elif choice == '4':
            tasks = [task for task in tasks if not task['completed']]
            print("Completed tasks removed.")
        elif choice == '5':
            save_tasks(tasks)
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def list_tasks(tasks):
    for index, task in enumerate(tasks):
        status = " [X] " if task['completed'] else " [ ] "
        print(f"{index}. {status}{task['task']}")

def save_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['completed']}\n")

if __name__ == "__main__":
    main()
