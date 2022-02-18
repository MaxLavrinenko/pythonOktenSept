# створити пустый список users_list = []
#
users_list = []
while True:
    print('1) додававання нового юзера')
    print('2) вивід всіх юзерів')
    print('3) вивід всіх юзерів за віком')
    print('4) видалення юзера по id')
    print('5) заміна статуса юзера на протилежний')
    print('6) вихід з меню')

    choise = int(input('Введите пункт меню : '))

    if choise not in [1, 2, 3, 4, 5, 6]:
        print('Нет такого пункта')
        continue
    if choise == 1:
        id = input('Введите ID : ')
        name = input('Имя юзера : ').capitalize()
        age = input('Возраст юзера : ')
        status = input('Статус юзера : ').capitalize()

        users_list.append({'id': id, 'name': name, 'age': age, 'status': status})
        continue
    elif choise == 2:
        print(users_list)
        continue

    elif choise == 3:
        users_list.sort(key=lambda x: x.get('age'))
        print(users_list)
        continue

    elif choise == 4:
        id = str(input('id= '))
        for i in users_list:
            if i['id'] == id:
                users_list.pop(users_list.index(i))
                print(users_list)
        continue

    elif choise == 5:
        for i in users_list:
            if i['status'] == 'True':
                i['status'] = 'False'
            elif i['status'] == 'False':
                i['status'] = 'True'
        print(users_list)
        continue

    elif choise == 6:
        break
# стврорити меню в якому потрібно реалізувати:
#
# 1) додававання нового юзера
# 2) вивід всіх юзерів
# 3) вивід всіх юзерів за віком
# 4) видалення юзера по id
# 5) заміна статуса юзера на протилежний
# 6) вихід з меню
#
# приклад юзера {'id':1,'name':'Max', 'age':35,'status':False}
