tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
def delete_task(index):
    try:
        tasks.pop(index - 1)
        print("Task deleted")
    except IndexError:
        print("Invalid task number")



def delete_task(index):
    tasks.pop(index)   # ❌ Bug: index should be index-1

def add_task(task):
    tasks.append(task)
    print("Task added")


if __name__ == "__main__":
    show_tasks()
