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



if __name__ == "__main__":
    show_tasks()
