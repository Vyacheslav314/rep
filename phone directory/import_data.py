def user_name_writing(data):
    with open('phone_directory.txt', 'a', encoding='utf-8') as file:
        file.write(f'{data} - ')

def phone_number_writing(data):
    with open('phone_directory.txt', 'a', encoding='utf-8') as file:
        file.write(f'{data} - ')

def comment_writing(data):
    with open('phone_directory.txt', 'a', encoding='utf-8') as file:
        file.write(f'{data}\n')
           