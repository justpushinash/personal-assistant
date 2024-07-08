reminders_list = []

def add_reminder():
    reminder = input("Введите напоминание: ")
    reminders_list.append(reminder)
    print("Напоминание добавлено.")

def view_reminders():
    if reminders_list:
        print("Ваши напоминания:")
        for idx, reminder in enumerate(reminders_list, 1):
            print(f"{idx}. {reminder}")
    else:
        print("У вас нет напоминаний.")

def delete_reminder():
    view_reminders()
    try:
        reminder_index = int(input("Введите номер напоминания для удаления: "))
        if 0 < reminder_index <= len(reminders_list):
            removed = reminders_list.pop(reminder_index - 1)
            print(f"Напоминание '{removed}' удалено.")
        else:
            print("Неверный номер.")
    except ValueError:
        print("Пожалуйста, введите число.")

        
        