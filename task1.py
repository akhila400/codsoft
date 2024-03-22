
def display_list(todo_list):
    if not todo_list:
        print("Your To-Do list is empty!")
    else:
        print("Your To-Do list:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")


def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added to your To-Do list.")


def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from your To-Do list.")
    else:
        print("Invalid task index!")


def main():
    todo_list = []

    while True:
        print("\nOptions:")
        print("1. Display To-Do list")
        print("2. Add task to To-Do list")
        print("3. Remove task from To-Do list")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_list(todo_list)
        elif choice == '2':
            task = input("Enter task to add: ")
            add_task(todo_list, task)
        elif choice == '3':
            task_index = int(input("Enter task index to remove: "))
            remove_task(todo_list, task_index)
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    main()
