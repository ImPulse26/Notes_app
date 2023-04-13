import file_operation
import class_Note

def create_note():
    title = input('Введите заголовок: ')
    body = input('Введите тело заметки: ')
    return class_Note.Note(title=title, body=body)

def add():
    note = create_note()
    array = file_operation.read_file()
    for notes in array:
        if class_Note.Note.get_id(note) == class_Note.Note.get_id(notes):
            class_Note.Note.set_id(note)
    array.append(note)
    file_operation.write_file(array, 'a')
    print('Заметка добавлена.')


def show(text):
    logic = True
    array = file_operation.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(class_Note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + class_Note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in class_Note.Note.get_date(notes):
                print(class_Note.Note.map_note(notes))
    if logic == True:
        print('Заметки отсутствуют.')


def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    array = file_operation.read_file()
    logic = True
    for notes in array:
        if id == class_Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = create_note()
                class_Note.Note.set_title(notes, note.get_title())
                class_Note.Note.set_body(notes, note.get_body())
                class_Note.Note.set_date(notes)
                print('Заметка отедактирована.')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена.')
            if text == 'show':
                print(class_Note.Note.map_note(notes))
    if logic == True:
        print('Такой заметки нет, проверьте id')
    file_operation.write_file(array, 'a')
