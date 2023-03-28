import phone_book

pb = phone_book.PhoneBook('phone_db.txt')
print(len(pb.phone_list))

while True:
    print(pb.menu())
    choice = input('Введите пункт меню: ')
    if choice.isdigit() and 0 < int(choice) <= 7:
        choice = int(choice)
    else:
        print(f'Введите ЧИСЛО от 1 до 7')

    match choice:
        case 1:
            print(pb)
        case 2:
            name = input('Введите имя: ')
            phone = input('Введите номер: ')
            comment = input('Введите комментарий: ')
            pb.new_contact(name, phone, comment)
        case 3:
            word = input('Введите поисковый запрос: ')
            print(pb.search(word))
        case 4:
            print(pb)
            index = input('Введите индекс контакта, который будем изменять: ')
            if index.isdigit() and 0 < int(index) <= len(pb.phone_list):
                index = int(index)
                name = input('Введите имя (или Enter, если хотите оставить его без изменения): ')
                phone = input('Введите номер(или Enter, если хотите оставить его без изменения): ')
                comment = input('Введите комментарий(или Enter, если хотите оставить его без изменения): ')
                pb.change(index - 1, name, phone, comment)
            else:
                print(f'Введите число от 0 до {len(pb.phone_list)}')

        case 5:
            print(pb)
            index = input('Введите индекс контакта, который хотите удалить: ')
            if index.isdigit() and 0 < int(index) <= len(pb.phone_list):
                index = int(index)
                pb.delete(index-1)
            else:
                print("Такого контакта нет")
        case 6:
            pb.save()
        case 7:
            break



            

