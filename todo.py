tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print("Task added")


if __name__ == "__main__":
    show_tasks()
