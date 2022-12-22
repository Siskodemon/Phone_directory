import data_base
import view


def nik_filter(soname, name, nik, phone):
    view.view_table(data_base.view_phone_numbers(soname, name, nik, phone))
