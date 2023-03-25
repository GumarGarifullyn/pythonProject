import view
import model

def start():
    while True:
        pb = model.get_phone_book()
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.show_message('Файл успешно открыт')
            case 2:
                if view.show_contact(pb, 'Телефонная книга пуста или не открыта'):
                    model.save_file()
                    view.show_message('Файл успешно сохранен')
            case 3:
                view.show_contact(pb, "Телефонная книга не открыта или пуста!")
            case 4:
                contact = view.add_contact()
                model.add_contact(contact)
                view.show_message('Контакт добавлен, не забудь его сохранить!')
            case 5:
                if view.show_contact(pb, 'Телефонная книга пуста или не открыта'):
                    index = view.input_index('Введите номер изменяемого контакта: ')
                    contact = view.change_contact(pb, index)
                    model.change_contact(contact, index)
                    view.show_message('Контакт изменен, не забудь его сохранить')
            case 6:
                search = view.input_search('Введите искомый элемент ')
                result = model.find_contact(search)
                view.show_contact(result, 'Контакт не найден')
            case 7:
                index = view.input_index('Введите номер контакта, который нужно удалить: ')
                model.delete_contact(index)
            case 8:
                view.show_message('Пока')
                return