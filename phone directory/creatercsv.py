def user_name_logger(data):
    with open('phone_directory.csv', 'a', encoding='utf-8') as file:
        file.write(f';{data}; ')

def phone_number_logger(data):
    with open('phone_directory.csv', 'a', encoding='utf-8') as file:
        file.write(f';{data}; ')

def comment_logger(data):
    with open('phone_directory.csv', 'a', encoding='utf-8') as file:
        file.write(f';{data};\n')
           