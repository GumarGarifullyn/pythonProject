import text_menu
def main_menu() -> int:
   print(text_menu.main_menu)
   lenght_menu = len(text_menu.main_menu.split('\n'))-1
   while True:
        choice = input("Выбери пункт меню: ")
        if choice.isdigit() and 0 < int(choice) <= lenght_menu:
            return int(choice)
        else:
            print(f'Введите ЧИСЛО от 1 до {lenght_menu}')

def show_contact(book: list[dict], error_message):
    if book:
        show_message("Телефонная книга:")
        for i, contact in enumerate(book, 1):
            print(f'{i}. {contact.get("name"):<15} '
                  f'{contact.get("phone"):<15} '
                  f'{contact.get("comment"):<15} ')
        print("="*len(f'{i}. {contact.get("name"):<15} '
                  f'{contact.get("phone"):<15} '
                  f'{contact.get("comment"):<15} '))
    else:
        show_message(error_message)


def add_contact() -> dict:
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комметарий: ')
    return {'name': name, 'phone': phone, 'comment': comment}

def input_index(message: str):
    return int(input(message))

def input_search(message):
    return input(message)
def change_contact(book: list[dict], index: int):
    print('Введите новые данные или оставьте пустое поле, чтобы оставить без изменений ')
    contact = add_contact()
    return {'name': contact.get('name') if contact.get('name') else book[index-1].get('name'),
            'phone': contact.get('phone') if contact.get('phone') else book[index-1].get('phone'),
            'comment': contact.get('comment') if contact.get('comment') else book[index-1].get('comment')}

def show_message(message: str):
    print('-'*len(message))
    print(message)
    print('-'*len(message))