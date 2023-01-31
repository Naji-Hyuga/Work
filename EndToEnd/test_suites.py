#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random as rand
import time
import os
import locators as l
import logic as f



subject = f.Subject(l.testsubject, 'ul', f.gen_inn_ul(), "200201423", f.gen_ogrn(), f.gen_snils())

phis_object = f.Test_object(l.testobject, subject.name, l.object_type1, "Предприятия общественного питания", 1)

smi_object = f.Test_object("SMI"+l.testobject, subject.name, l.object_type2, "Интернет-радио", 1)

retsmi_object = f.Test_object("RSMI"+l.testobject, subject.name, l.object_type2, "Интернет-радио", 0)

phis_object_kgz = f.Test_object(l.testobject, subject.name, l.object_type1, "Общепит", 1)


def fixrate():
    f.create_contract(subject.name, 'Предприятия общественного питания')
    f.add_common_condition('01012021')
    f.add_object_rate_fix(phis_object.name)
    f.activate_contract(l.cont_number)
    f.ident_payment(l.cont_number, l.testpayment)
    f.search_contrat(l.cont_number)
    f.compare_accurals(l.cont_number, l.testpayment)
    f.add_report(l.cont_number, phis_object.name, "mp")
    return True

def translate_smi_contract():
    f.create_contract(subject.name, 'Интернет-радио')
    f.add_common_condition('01012021')
    f.add_percent_rate_object(smi_object.name)
    f.activate_contract(l.cont_number)
    f.ident_payment(l.cont_number, l.testpayment)
    f.add_report(l.cont_number, phis_object.name, "trk")
    f.search_contrat(l.cont_number)
    f.compare_accurals(l.cont_number, l.testpayment)


# Smoke test / Условия договора. Ставка по объекту, закрытие начислений
def smoke_object_rate_and_close():
    f.add_contract('VOIS', 'Предприятия общественного питания', '01012021', '31122021')
    f.add_common_condition('01012021')
    f.add_obj_rate(1, 'fix', '01012021', 'ооо', 100, '0106', '3006', 200)
    f.activate_contract2()
    f.check_accurals_type('rew_obj', 12)
    f.check_accurals_values('100', 11)
    f.check_accurals_values('200', 1)
    f.close_accurals(1)
    f.agree_on_termination()
    f.on_termination()
    f.close_accurals('all')
    f.agree_on_close()
    f.on_close()
    f.click(l.contracts)
    return True


# Smoke test / Условия договора. Ставка по договору, генерация начислений
def smoke_generation_on_period():
    f.add_contract('VOIS', 'Предприятия общественного питания', '01012021', '30062022')
    f.add_common_condition('01012021')
    f.add_contract_rate('fix', '01072021', 100)
    f.activate_contract2()
    f.check_accurals_type('rew_cont', 12)
    f.check_accurals_values('100', 12)
    f.close_accurals(3)
    f.generic_accurals_on_period('three', 'n')
    f.check_accurals_type('rew_cont', 12)
    f.check_accurals_values('100', 12)
    f.close_accurals('all')
    f.generic_accurals_on_period('six', 'n')
    f.check_accurals_type('rew_cont', 6)
    f.check_accurals_values('100', 6)
    f.close_accurals(3)
    f.generic_accurals_on_period('nine', 'n')
    f.check_accurals_type('rew_cont', 12)
    f.check_accurals_values('100', 12)
    f.close_accurals('all')
    f.generic_accurals_on_period('twelve', 'n')
    f.check_accurals_type('rew_cont', 12)
    f.check_accurals_values('100', 12)
    f.click(l.contracts)
    return True


# Smoke test / Создание дополнительного соглашения
def smoke_create_additional_agree():
    f.add_contract('VOIS', 'Предприятия общественного питания', '01012021', '31122021')
    f.add_common_condition('01012021')
    f.add_obj_rate(2, 'fix', '01012021', 'ооо', 100, 'n', 'n', 'n')
    f.add_obj_rate(1, 'fix', '01012021', 'бар', 100,  '0106', '3006', 200)
    f.activate_contract2()
    f.create_additional_agree('01012021')
    f.exeption_rate('obj_fix', 'ооо', 0, 'n', 'main')
    f.exeption_rate('obj_fix', 'бар', 0, 'yes','n')
    f.add_obj_rate(1, 'fix', '01022021', 'рес', 100, 'n', 'n', 'n')
    f.activate_additional_doc()
    f.check_cond_filter_work('rate', 'delete', 'n', 0, 3)
    f.check_cond_filter_work('n', 'n', '1', 0, 3)
    f.check_accurals_type('rew_obj', 12)
    f.check_accurals_values('300', 11)
    f.check_accurals_values('200', 1)
    f.click(l.contracts)
    return True


# Smoke test / Разовые начисления
def smoke_one_off_accurals():
    f.add_contract('VOIS', 'Предприятия общественного питания', '01012021', '31122021')
    f.add_common_condition('01012021')
    f.add_contract_rate('fix', '01012021', '100')
    f.activate_contract2()
    f.add_one_of_accurals('fine', '123,45')
    f.add_one_of_accurals('penalty', '123,45')
    f.add_one_of_accurals('debit_debt', '123,45')
    f.add_one_of_accurals('comp_pre_judical', '123,45')
    f.add_one_of_accurals('comp_judical', '123,45')
    f.add_one_of_accurals('accomp_music', '123,45')
    f.add_one_of_accurals('big_license', '123,45')
    f.check_accurals_values('123,45', 7)
    f.check_accurals_values('100', 12)
    f.check_accurals_type('rew_cont', 12)
    f.close_accurals('all')
    f.click(l.contracts)
    return True


# Smoke test / Комбинированные начисления
def smoke_combo_accurals():
    f.add_contract('VOIS', 'Предприятия общественного питания', '01012021', '31122021')
    f.add_common_condition('01012021')
    f.add_obj_rate(1, '25', '01012021', 'бар', '100', 'n', 'n', 'n')
    f.activate_contract2()
    f.ident_payment_new(l.testpayment)
    f.create_accural_report('mp%', '01012021', '31012021',  25, 100, 100)
    f.check_acc_in_compars_values('100', 1)
    f.check_acc_in_compars_type('rew_repo', 1)
    f.check_accurals_values('100', 1)
    f.check_accurals_type('rew_repo', 1)
    f.add_one_of_accurals('fine', '123.45')
    f.add_one_of_accurals('penalty', '123.45')
    f.add_one_of_accurals('debit_debt', '123.45')
    f.add_one_of_accurals('comp_pre_judical', '123.45')
    f.add_one_of_accurals('comp_judical', '123.45')
    f.add_one_of_accurals('accomp_music', '123.45')
    f.add_one_of_accurals('big_license', '123.45')
    f.check_one_off_in_comparsion('all', 1)
    f.check_acc_in_compars_values('123,45', 7)
    f.create_additional_agree('01012021')
    f.add_contract_rate('fix', '01012021', 100)
    f.add_obj_rate(2, 'fix', '01012021', 'ооо', 100, 'n', 'n', 'n')
    f.activate_additional_doc()
    f.check_acc_in_compars_values('100', 13)
    f.check_acc_in_compars_values('200', 12)
    f.check_acc_in_compars_type('rew_obj', 12)
    f.check_acc_in_compars_type('rew_cont', 12)
    f.check_accurals_values('100', 13)
    f.check_accurals_values('200', 12)
    f.check_accurals_type('rew_obj', 12)
    f.check_accurals_type('rew_cont', 12)
    f.write_off_accurals(0, 'debit_debt', 50)
    f.write_off_accurals(0, 'pause', 50)
    f.check_accurals_values('100', 12)
    f.check_acc_in_compars_values('100', 12)
    f.write_off_accurals(1, 'debit_debt', 200)
    f.write_off_accurals(3, 'pause', 200)
    f.check_accurals_values('200', 10)
    f.check_acc_in_compars_values('200', 10)
    f.del_report(1)
    f.check_acc_in_compars_type('rew_repo', 0)
    f.check_accurals_type('rew_repo', 0)
    f.close_accurals('all')
    f.click(l.contracts)
    return True


# Smoke test / Коэффициент
def smoke_koefficient():
    f.add_contract('VOIS' ,'Предприятия общественного питания', '01012021', '31122021')
    f.add_common_condition('01012021')
    f.add_contract_rate('fix', '01012021', '100')
    f.add_obj_rate(1, 'fix', '01012021', 'ооо', '100', 'n', 'n', 'n')
    f.add_koefficets('network', 0, '01012021', '30062021')
    f.add_koefficets('stimul', 1, '01012021', '31032021')
    f.activate_contract2()
    f.check_accurals_type('rew_obj', 12)
    f.check_accurals_type('rew_cont', 12)
    f.check_accurals_values('85,5', 6)      # 0.9*0.95*100
    f.check_accurals_values('95', 6)        # 0.95*100
    f.check_accurals_values('100', 12)
    f.create_additional_agree('01012021')
    f.add_koefficets('network', 4, '01042021', 'n')
    f.add_koefficets('stimul', 3, '01032021', '31052021')
    f.activate_additional_doc()
    f.check_accurals_type('rew_obj', 12)
    f.check_accurals_type('rew_cont', 12)
    f.check_accurals_values('85,5', 4)     # 0.9*0.95*100
    f.check_accurals_values('76', 2)        # 0.8*0.95*100
    f.check_accurals_values('64', 4)        # 0.8*0.8*100
    f.check_accurals_values('80', 14)       # 0.8*100
    f.click(l.contracts)
    return True


# Smoke test / Услуги
def smoke_services():
    f.choose_profile('FORMAX')
    f.add_contract('FORMAX', 'Предприятия общественного питания', '01012021', '31122021')
    f.add_common_condition('01012021')
    f.add_service('one_off', '01012021', 'n', 123.45)
    f.checklen(f.get_list(l.elem_service), 1)
    f.add_service('n', '01022021', '31082021', 100)
    f.checklen(f.get_list(l.elem_service), 2)
    f.activate_contract2()
    f.check_accurals_type('service', 8)
    f.check_accurals_values('123,45', 1)
    f.check_accurals_values('100', 7)
    f.create_additional_agree('01012021')
    f.add_service('n', '01032021', 'n', '200')
    f.activate_additional_doc()
    f.check_accurals_type('service', 12)
    f.check_accurals_values('123,45', 1)
    f.check_accurals_values('100', 1)
    f.check_accurals_values('200', 10)
    f.close_accurals('all')
    f.click(l.contracts)
    return True


# Smoke test / Начисления в Формакс
def smoke_accurals_in_formax():
    f.choose_profile('FORMAX')
    f.add_contract('FORMAX', 'Предприятия общественного питания', '01012021', '31122021')
    f.add_common_condition('01012021')
    f.add_object_rate_formax(2, 'fix', 'ооо', 1, '01012021','100', 'n', 'n', 'n', 'n')
    f.add_service('n', '01012021', 'n', '123.45')
    f.activate_contract2()
    f.check_accurals_type('service', 12)
    f.check_accurals_values('123,45', 12)
    f.check_accurals_values('500', 12)
    f.accural_arrow_info()
    time.sleep(2)
    f.checklen(f.get_list(l.values_into_accural), 5)
    f.accural_arrow_info()
    f.check_switcher_period()
    f.close_accurals('all')
    f.click(l.contracts)
    return True


# Smoke test / Отчёт Мелкая публичка
def smoke_small_pub_per():
    f.add_contract('VOIS', 'Предприятия общественного питания', '01012021', '31122021')
    f.add_common_condition('01012021')
    f.add_obj_rate(2, '25', '01012021', 'ооо', "123.45", 'n', 'n', 'n')
    f.activate_contract2()
    f.create_accural_report('mp%', '01012021', '31012021', 25, 500, '246.90')
    f.check_accurals_values('246,90', 1)
    f.check_accurals_type('rew_repo', 1)
    f.del_report(1)
    f.check_accurals_type('rew_repo', 0)
    f.click(l.contracts)
    return True


# Smoke test / Отчёт ТРК
def smoke_trk_report():
    f.add_contract('VOIS', 'Интернет-радио', '01012021', '31122021')
    f.add_common_condition('01012021')
    f.add_contract_rate(25, '01012021', '123,45')
    f.add_obj_rate(1, '25', '01012021', 'ретран', "267,55", 'n', 'n', 'n')
    f.add_obj_rate(1, '0', '01012021', 'эфир', "0", 'n', 'n', 'n')
    f.activate_contract2()
    f.create_accural_report('trk', '01012021', '31012021', 25, 2000, 500)
    f.check_accurals_type('rew_repo', 1)
    f.check_accurals_values('500', 1)
    f.create_additional_agree('01012021')
    f.exeption_rate('obj_perc', 'ретран', 0, 'n', 'main')
    f.activate_additional_doc()
    f.create_accural_report('trk', '01022021', '28022021', 25, '493,8', '123,45')
    f.check_accurals_type('rew_repo', 2)
    f.check_accurals_values('123,45', 1)
    f.click(l.contracts)
    return True


# Smoke / Дневные ставки
def smoke_day_rates():
    f.choose_profile('FORMAX')
    f.add_contract('FORMAX', 'Предприятия общественного питания', '01012021', '31122021')
    f.add_common_condition('01012021')
    f.add_object_rate_formax(2, 'fix', 'ооо', 1, '01012021','100', '0107', '3108', '200', 'n')
    # f.add_object_rate_formax(2, 'day', 'ооо',  0, '01012021','10', 'n', 'n', 'n', 31)
    return True

# Smoke / Проверка связей отчётов и начислений
def connect_repo_and_accural():
    f.add_contract('VOIS', 'Предприятия общественного питания', '01012021', '31122021')
    f.add_common_condition('01012021')
    f.add_obj_rate(2, 'fix', '01012021', 'ооо', "123.46", 'n', 'n', 'n')
    f.activate_contract2()
    f.create_accural_report('mp', '01012021', '31012021', 'n', 'mp', "246.92")
    f.create_accural_report('mp', '01022021', '28022021', 'n', 'mp', "246.92")
    f.check_accural_report_connect('246,92', 2, 2)
    f.del_report(2)
    f.check_accural_report_connect(0, 12, 0)
    f.click(l.contracts)
    return True

# f.search_contrat("AU0318102038")
