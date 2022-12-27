import data_base
import view

def nik_filter(soname, name, nik, phone):
    view.view_table(data_base.view_phone_numbers(soname, name, nik, phone))

def ins_con_in_db(soname, name, patr, nik, age, gender, nationality, phone):
    view.view_ins_cont_result(data_base.ins_user_in_db(soname, name, patr, nik, age, gender, nationality, phone))

def delete_contact(nik):
    view.delet_user_result(data_base.delete_user(nik))

def Give_nik_to_controller(nikname):
    return view.Show_phone_numbers(data_base.Give_phone_data_to_controller(nikname))

def Put_contact_date_to_view(result):
    return view.Show_data_contact(result)
