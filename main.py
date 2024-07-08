import reminders
import tasks
import quotes

def main():
    print("Добро пожаловать в Личного помощника!")
    while True:
        print("\nВыберите действие:")
        print("1. Напоминания")
        print("2. Планировщик задач")
        print("3. Генератор цитат")
        print("4. Погода")
        print("5. Выход")
        choice = input("Ваш выбор: ")

        if choice == '1':
            manage_reminders()
        elif choice == '2':
            manage_tasks()
        elif choice == '3':
            quotes.generate_quote()
        elif choice == '4':
            print("Получение данных о погоде")
            # Здесь будет вызов функции для получения данных о погоде
        elif choice == '5':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

def manage_reminders():
    while True:
        print("\nМеню напоминаний:")
        print("1. Добавить напоминание")
        print("2. Просмотреть напоминания")
        print("3. Удалить напоминание")
        print("4. Назад в главное меню")
        choice = input("Ваш выбор: ")

        if choice == '1':
            reminders.add_reminder()
        elif choice == '2':
            reminders.view_reminders()
        elif choice == '3':
            reminders.delete_reminder()
        elif choice == '4':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

def manage_tasks():
    while True:
        print("\nМеню задач:")
        print("1. Добавить задачу")
        print("2. Просмотреть задачи")
        print("3. Удалить задачу")
        print("4. Назад в главное меню")
        choice = input("Ваш выбор: ")

        if choice == '1':
            tasks.add_task()
        elif choice == '2':
            tasks.view_tasks()
        elif choice == '3':
            tasks.delete_task()
        elif choice == '4':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()


