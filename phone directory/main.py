from re import S
import interface
import logger as log
import search as sea

if interface.user == 4:
    log.user_name_view()
    log.phone_number_view()
    log.comment_view()
if interface.user == 1:
    a = interface.serch_data(interface.s)
    print(a)
