import data_base
import view

def nik_filter(soname, name, nik, phone):
    view.view_table(data_base.view_phone_numbers(soname, name, nik, phone))

def ins_con_in_db(soname, name, patr, nik, age, gender, nationality, phone):
    view.view_ins_cont_result(data_base.ins_user_in_db(soname, name, patr, nik, age, gender, nationality, phone))

def delete_contact(nik):
    view.delet_user_result(data_base.delete_user(nik))
