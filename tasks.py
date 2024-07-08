tasks_list = []

def add_task():
    task = input("Введите задачу: ")
    deadline = input("Введите дедлайн (например, 2024-12-31): ")
    tasks_list.append({"task": task, "deadline": deadline})
    print("Задача добавлена.")

def view_tasks():
    if tasks_list:
        print("Ваши задачи:")
        for idx, task in enumerate(tasks_list, 1):
            print(f"{idx}. {task['task']} - дедлайн: {task['deadline']}")
    else:
        print("У вас нет задач.")

def delete_task():
    view_tasks()
    try:
        task_index = int(input("Введите номер задачи для удаления: "))
        if 0 < task_index <= len(tasks_list):
            removed = tasks_list.pop(task_index - 1)
            print(f"Задача '{removed['task']}' удалена.")
        else:
            print("Неверный номер.")
    except ValueError:
        print("Пожалуйста, введите число.")
