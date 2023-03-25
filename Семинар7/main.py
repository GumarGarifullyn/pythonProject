def open_fail():
    path = r'data.txt'
    file = open(path, 'r', encoding="UTF-8")
    list_num = file.readlines()
    print(list_num)
    print(list_num[0])
    lib_num = {}
    for index in range(len(list_num)):
        temp = list_num[index].split(':')
        lib_temp = {temp[1]: temp[2], temp[3]: temp[4]}
        lib_num[temp[0]] = lib_temp
        print(temp[0])
        print(lib_num)
        return lib_num
open_fail()
name = input('Введите имя: ')
print(lib_num.get(name, 'нет такого контакта'))
if lib_num.get(name) == None:
    job = input('Введите рабочий номер контакта: ')
    user = input('Введите личный номер контакта :')
    new_cont = {"рабочий" : job, " личный" : user}
    print(lib_num.setdefault(name, new_cont))

print(lib_num)




