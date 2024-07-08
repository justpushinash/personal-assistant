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
            print("Работа с напоминаниями")
        elif choice == '2':
            print("Работа с задачами")
        elif choice == '3':
            print("Генерация случайных цитат")
        elif choice == '4':
            print("Получение данных о погоде")
        elif choice == '5':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")
            

if __name__ == "__main__":
    main()