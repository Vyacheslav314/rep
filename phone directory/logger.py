import creatercsv as cre
import interface as inter
import import_data as idata

def user_name_view():
    data = inter.data_user_name()
    cre.user_name_logger(data)
    idata.user_name_writing(data)
    return data

def phone_number_view():
    data = inter.data_phone_number()
    cre.phone_number_logger(data)
    idata.phone_number_writing(data)
    return data

def comment_view():
    data = inter.data_comment()
    cre.comment_logger(data)
    idata.comment_writing(data)
    return data