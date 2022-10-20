import search as sea
print('Поиск по фамилии введите 1:')
print('Поиск по номеру введите 2:')
print('Поиск по коментарию введите 3:')
print('Добавить пользователя введите 4:')
print('Удалить пользователя введите 5:')
user = int(input())
if user == 1:
    print('Введите фио: ')
    s = input()
    def serch_data(s):
        for line in sea.serch_user_name():
            if line == s:
                return print(line)
if user == 2:
    print('Введите номер телефона: ')
    s = input()
    def serch_data(s):
        for line in sea.serch_user_name():
            if line == s:
                return print(line)
if user == 3:
    print('Введите коментарий: ')
    s = input()
    def serch_data(s):
        for line in sea.serch_user_name():
            if line == s:
                return print(line)
if user == 4:
    
    def data_user_name():
        user_name = input('Введите фио: ')
        return user_name

    def data_phone_number():
        phone_number = input('Введите номер телефона: ')
        return phone_number

    def data_comment():
        comment = input('Введите коментарий: ')
        return comment
if user == 5:
    print('Введите фио что бы удалить пользователя: ')
    s = input()
