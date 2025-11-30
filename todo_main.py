from todo_manager import add_todo, list_todos, mark_done, delete_todo

MENU = """
--- To-Do List ---
1. Add task
2. List tasks
3. List pending tasks
4. Mark task done
5. Delete task
6. Exit
Choose an option: """

def input_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        return None

def show_task(t):
    status = "✓" if t["done"] else " "
    print(f"[{status}] {t['id']}. {t['title']} - {t.get('description','')}")

def main():
    while True:
        choice = input(MENU).strip()
        if choice == "1":
            title = input("Task title: ").strip()
            desc = input("Description (optional): ").strip()
            todo = add_todo(title, desc)
            print("Added task:")
            show_task(todo)
        elif choice == "2":
            todos = list_todos(show_all=True)
            print(f"\nAll tasks ({len(todos)}):")
            for t in todos:
                show_task(t)
            print()
        elif choice == "3":
            todos = list_todos(show_all=False)
            print(f"\nPending tasks ({len(todos)}):")
            for t in todos:
                show_task(t)
            print()
        elif choice == "4":
            tid = input_int("Enter task id to mark done: ")
            if tid is None:
                print("Invalid id.")
                continue
            if mark_done(tid):
                print("Marked done.")
            else:
                print("Task not found.")
        elif choice == "5":
            tid = input_int("Enter task id to delete: ")
            if tid is None:
                print("Invalid id.")
                continue
            if delete_todo(tid):
                print("Deleted.")
            else:
                print("Task not found.")
        elif choice == "6":
            print("Bye!")
            break
        else:
            print("Unknown option. Please choose 1-6.")

if __name__ == "__main__":
    main()
