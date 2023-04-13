import function as f


def menu():
    while True:
        print(f"\nЗаметки\n{'*' * 27}")
        main_menu = input("1. Показать все заметки\n"
                        "2. Добавить заметку\n"
                        "3. Редактировать заметку\n"
                        "4. Удалить заметку\n"
                        "5. Выборка заметок по дате\n"
                        "6. Показать заметку по id\n"
                        "7. Выход\n")
        match main_menu:
            case "1":
                f.show('all')
            case "2":
                f.add()
            case "3":
                f.show('all')
                f.id_edit_del_show('edit')
            case "4":
                f.show('all')
                f.id_edit_del_show('del')
            case "5":
                f.show('date')
            case "6":
                f.show('id')
                f.id_edit_del_show('show')
            case "7":
                print("Работа программы завершена")
                break
