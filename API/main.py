#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv
import os
import requests
import openpyxl
import json
import time
import api_tests as t
import crm_api as c


# a, x = argv
x = "create"

send = "n"  # Переменная отвечает за отправку отчетов сразу после создания (y/n)


def requestPost(url, json_query, headers):
    r = requests.post(url, data=json.dumps(json_query), headers=headers)
    return r


def requestGet(url, payload, headers):
    r = requests.get(url, params=payload, headers=headers)
    return r


# # Выбор тестовых данных для заданного сервера
# if c.server == 'preprod':
#     c.preprod_subjects["ru"] = t.find(c.getsubjlist, c.getsubjlist_query, "ААА Тест Кейс", "s")
#     c.preprod_ojects['rate']["id"] = t.find(c.getobjlist, c.getsubjlist_query, "Бар Хмельной Топаз", "o")
#     c.preprod_ojects['trk']["id"] = t.find(c.getobjlist, c.getobjlist_query, "Транслятор AUtest СМИ", "o")
#     c.preprod_ojects['trkr']["id"] = t.find(c.getobjlist, c.getobjlist_query, "Ретранслятор AUtest СМИ", "o")
#     c.preprod_ojects['avp']["id"] = t.find(c.getobjlist, c.getobjlist_query, "Кинотеатр стрела", "o")
#     c.preprod_ojects['fil']["id"] = t.find(c.getobjlist, c.getobjlist_query, "Дом культуры Смена", "o")
#     # c.preprod_ojects['event']["id"] = t.find(c.geteventlist, c.getobjlist_query, "концерт Руки Вверх", "e")
#     c.objects = c.preprod_ojects
#     c.subjects = c.preprod_subjects
# if c.server == 'hotfix':
#     c.hotfix_subjects["ru"] = t.find(c.getsubjlist, c.getsubjlist_query, "ААА Тест Кейс", "s")
#     c.hotfix_objects['rate']["id"] = t.find(c.getobjlist, c.getobjlist_query, "Бар Хмельной Топаз", "o")
#     c.hotfix_objects['trk']["id"] = t.find(c.getobjlist, c.getobjlist_query, "Транслятор AUtest СМИ", "o")
#     c.hotfix_objects['trkr']["id"] = t.find(c.getobjlist, c.getobjlist_query, "Ретранслятор AUtest СМИ", "o")
#     c.hotfix_objects['avp']["id"] = t.find(c.getobjlist, c.getobjlist_query, "Кинотеатр стрела", "o")
#     c.hotfix_objects['fil']["id"] = t.find(c.getobjlist, c.getobjlist_query, "Дом культуры Смена", "o")
#     # c.hotfix_objects['event']["id"] = t.find(c.geteventlist, c.getobjlist_query, "концерт Руки Вверх")
#     c.objects = c.hotfix_objects
#     c.subjects = c.hotfix_subjects
# if c.server == 'bel':
#     c.subjects = c.bel_subjects
#     c.objects = c.bel_objects
# if c.server == 'kz':
#     c.subjects = c.kz_subjects
#     c.objects = c.kz_objects


# c.addCont_data["subject_id"] = c.subjects['ru']
# c.addRateCond_payload["useobject_id"] = c.objects["rate"]["id"]
# c.addPercentcond_data["useobject_id"] = c.objects["trk"]["id"]
# c.addEvent_data["event_id"] = c.objects["event"]["id"]
# c.mp_report_data["useobject_ids[]"] = c.objects["rate"]["id"]
# c.addretransalor_data["translator_id"] = c.objects["trk"]["id"]
# c.addretransalor_data["useobject_id"] = c.objects["trkr"]["id"]
# c.mpr_report_data["useobject_ids[]"] = c.objects["rate"]["id"]
# c.mp_event_data["event_useobject_id"] = c.objects["rate"]["id"]
# c.event_report_data["event_id"] = c.objects["event"]["id"]
# c.fil_report_data["event_useobject_id"] = c.objects["fil"]["id"]
# c.avp_report_data["useobject_ids[]"] = c.objects["avp"]["id"]


if x == "trk" or x == "all":
    # Создание договора и отчета ТРК транслятора
    print("Создаем отчет ТРК транслятор")
    addCont_data = c.addCont_data

    t.addContract(c.category["trk"], addCont_data)

    t.add_commonrate_condition(c.addComCond, c.addComCond_payload)

    t.add_commonrate_condition(c.addRateCond, c.addPercentcond_data)

    t.activate_contract(t.context)

    c.trk_report_data["useobject_ids[]"] = c.objects["trk"]["id"]
    c.trk_report_data["report_file"][0]["useobject_id"] = c.objects["trk"]["id"]
    c.trk_report_data["useobject_percents"] = '[{"name":"%s","useobject_id":"%s","percent":100}]' % (c.objects["trk"]["name"], c.objects["trk"]["id"])
    t.add_report(t.context, c.trk_report_data)
    time.sleep(2)

    t.ident_payment(t.context, c.identAdd_data)

    t.calc_execute(t.context, c.calcExecute_data)
    if send == "y":
        t.send_report(t.context['report_id'])


if x == "trkr" or x == "all":
    # Создание договора и отчета ТРК ретранслятора
    print("Создаем отчет ТРК ретранслятор")
    addCont_data = c.addCont_data

    t.addContract(c.category["trk"], addCont_data)

    t.add_commonrate_condition(c.addComCond, c.addComCond_payload)

    addPercentcond_data = c.addPercentcond_data
    addPercentcond_data["useobject_id"] = c.objects["trkr"]["id"]
    t.add_commonrate_condition(c.addRateCond, addPercentcond_data)

    t.activate_contract(t.context)

    c.trk_report_data["useobject_ids[]"] = c.objects["trkr"]["id"]
    c.trk_report_data["report_file"][0]["useobject_id"] = c.objects["trkr"]["id"]
    c.trk_report_data["useobject_percents"] = '[{"name":"%s","useobject_id":"%s","percent":100}]' % (c.objects["trkr"]["name"], c.objects["trkr"]["id"])

    t.add_report(t.context, c.trk_report_data)
    time.sleep(3)

    t.ident_payment(t.context, c.identAdd_data)

    t.calc_execute(t.context, c.calcExecute_data)
    if send == "y":
        t.send_report(t.context['report_id'])


if x == "mp" or x == "all":
    # Создание отчета мелкая публичка
    print("\n", "Создаем отчет МП")
    t.addContract(c.category["mp"], c.addCont_data)
    # t.addContract(c.category_bel["mp"], c.addCont_data)
    t.add_commonrate_condition(c.addComCond, c.addComCond_payload)

    t.add_commonrate_condition(c.addRateCond, c.addRateCond_payload)

    t.activate_contract(t.context)

    t.ident_payment(t.context, c.identAdd_data)

    t.calc_execute(t.context, c.calcExecute_data)

    t.add_report(t.context, c.mp_report_data)
    if send == "y":
        t.send_report(t.context['report_id'])


if x == "mpr" or x == "all":
    # Распределение без отчета
    print("\n", "Создаем отчет на рейтинг")
    t.addContract(c.category["mp"], c.addCont_data)

    t.add_commonrate_condition(c.addComCond, c.addComCond_payload)

    t.add_commonrate_condition(c.addRateCond, c.addRateCond_payload)

    t.activate_contract(t.context)

    t.ident_payment(t.context, c.identAdd_data)

    t.calc_execute(t.context, c.calcExecute_data)

    t.add_report(t.context, c.mpr_report_data)
    if send == "y":
        t.send_report(t.context['report_id'])


if x == "event" or x == "all":
    # Отчет мероприятие
    print("\n", "Создаем отчет по мероприятию.")
    t.addContract(c.category["event"], c.addCont_data)

    t.add_commonrate_condition(c.addComCond, c.addComCond_payload)

    t.add_commonrate_condition(c.addEvent_url, c.addEvent_data)

    t.activate_contract(t.context)

    t.add_report(t.context, c.event_report_data)

    t.ident_payment(t.context, c.identAdd_data)

    t.calc_execute(t.context, c.calcExecute_data)
    if send == "y":
        t.send_report(t.context['report_id'])


if x == "event_f" or x == "all":
    # Отчет мероприятие бесплатный вход
    print("\n", "Создаем отчет по мероприятию бесплатный вход")
    t.addContract(c.category["event"], c.addCont_data)

    t.add_commonrate_condition(c.addComCond, c.addComCond_payload)

    t.add_commonrate_condition(c.addEvent_url, c.addEvent_data)

    t.activate_contract(t.context)

    event_report_data = c.event_report_data
    event_report_data["rate"] = "0"
    event_report_data["sum_income"] = "0"
    event_report_data["event_free_entry"] = "1"
    event_report_data["on_fixed_sum"] = "1"
    t.add_report(t.context, event_report_data)

    t.ident_payment(t.context, c.identAdd_data)

    t.calc_execute(t.context, c.calcExecute_data)
    if send == "y":
        t.send_report(t.context['report_id'])


if x == "event_n" or x == "all":
    # Отчет мероприятие не охраняется
    print("\n", "Создаем отчет по мероприятию не охраняется")
    t.addContract(c.category["event"], c.addCont_data)

    t.add_commonrate_condition(c.addComCond, c.addComCond_payload)

    t.add_commonrate_condition(c.addEvent_url, c.addEvent_data)

    t.activate_contract(t.context)

    event_report_data = c.event_report_data
    event_report_data["event_not_guarded"] = "1"
    event_report_data["rate"] = "0"
    event_report_data["sum_income"] = "0"
    event_report_data["sum_estimated"] = "0"
    event_report_data["sum_report"] = "0"
    t.add_report(t.context, c.event_report_data)
    if send == "y":
        t.send_report(t.context['report_id'])


if x == "mp_event" or x == "all":
    # Отчет мероприятие мелкая публичка
    print("\n", "Создаем отчет мероприятие мелкая публичка")
    t.addContract(c.category["mp"], c.addCont_data)

    t.add_commonrate_condition(c.addComCond, c.addComCond_payload)

    t.add_commonrate_condition(c.addRateCond, c.addRateCond_payload)

    t.activate_contract(t.context)

    t.add_report(t.context, c.mp_event_data)

    t.ident_payment(t.context, c.identAdd_data)

    t.calc_execute(t.context, c.calcExecute_data)
    if send == "y":
        t.send_report(t.context['report_id'])


if x == "avp" or x == "all":
    # Отчет АВП
    print("\n", "Создаем отчет по АВП")
    t.addContract(c.category["avp"], c.addCont_data)

    t.add_commonrate_condition(c.addComCond, c.addComCond_payload)

    addPercentcond_data = c.addPercentcond_data
    addPercentcond_data["useobject_id"] = c.objects['avp']["id"]
    t.add_commonrate_condition(c.addRateCond, addPercentcond_data)

    t.activate_contract(t.context)

    t.add_report(t.context, c.avp_report_data)

    t.ident_payment(t.context, c.identAdd_data)

    t.calc_execute(t.context, c.calcExecute_data)
    if send == "y":
        t.send_report(t.context['report_id'])


if x == "fil" or x == "all":
    # Отчет филармонии
    print("\n", "Создаем отчет по филармонии")
    t.addContract(c.category["fil"], c.addCont_data)

    t.add_commonrate_condition(c.addComCond, c.addComCond_payload)

    addPercentcond_data = c.addPercentcond_data
    addPercentcond_data["useobject_id"] = c.objects['fil']["id"]
    t.add_commonrate_condition(c.addRateCond, addPercentcond_data)

    t.activate_contract(t.context)

    t.add_report(t.context, c.fil_report_data)

    t.ident_payment(t.context, c.identAdd_data)

    t.calc_execute(t.context, c.calcExecute_data)
    if send == "y":
        t.send_report(t.context['report_id'])


if x == "izr":
    # Отчет ИЗР
    print("Создание ведомости")
    addCont_data = c.addCont_data
    addCont_data["subject_id"] = c.subjects['sw']
    t.addContract(c.category["izr"], addCont_data)
    t.add_commonrate_condition(c.addComCond, c.addComCond_payload)
    t.add_commonrate_condition(c.addRateCond, c.addRateCond_payload)
    t.activate_contract(t.context)
    t.ident_payment(t.context, c.identAdd_data)
    t.add_register(t.context, c.register_data)
    if send == "y":
        t.send_report(t.context['report_id'])


if x == "help":
    print("\n", "mp", "\n", "mpr", "\n", "mp_event", "\n", "trk", "\n", "avp", "\n", "fil", "\n", "event", "\n", "event_f", "\n", "event_n", "\n", "all", "\n", "create")


if x == "calc":
    # Создание договора со ставкой по объекту фикс и двумя сопставленными начислениями,
    # одно сопоставлено полностью, второе частично
    print("\n", "Создаем договор для среза начисления и оплата")
    t.addContract(c.category["mp"], c.addCont_data)

    t.add_commonrate_condition(c.addComCond, c.addComCond_payload)

    t.add_commonrate_condition(c.addRateCond, c.addRateCond_payload)

    t.activate_contract(t.context)

    t.ident_payment(t.context, c.identAdd_data)

    t.calc_execute(t.context, c.calcExecute_data)
    t.calc_execute2(t.context, c.calcExecute_data)


if x == "pay":
    pays = openpyxl.load_workbook('./Autotests/TestFiles/rao_pay_test.xlsx')
    sheets = pays.sheetnames
    pays.active = 1
    sheet = pays.active
    sheet['A2'] = "Test"+t.number
    cell = sheet['A2']
    print(cell.value)
    pays.save('./Autotests/TestFiles/rao_pay_test.xlsx')
    load_payment_data = c.load_payment_data
    pfiles = {'file' : open('./Autotests/TestFiles/rao_pay_test.xlsx', 'rb')}
    t.load_payment(load_payment_data, pfiles)



if x == 'test':
    num = 32 // 3
    phrase = 'Hello' if num == 10 else 'World'
    print('-'.join(phrase[::-1]))




if x == "del_contracts":    # УДаление договоров или допников из файла
    def delete_quotes(x):
        a = x.readlines()
        k = []
        for i in a[:]:
            j = i.strip()
            k.append(j)
        return k

    base = open("01.05.21FM.txt", "r", encoding='utf-8')

    contract_list = delete_quotes(base)

    base.close()

    cont_del_data = c.cont_del_data
    count = 0
    for i in contract_list:
        cont_del_data['id'] = i
        res = requestPost(c.cont_del_url, cont_del_data, t.headers)
        count += 1
        print(json.loads(res.text))

    print("Обработано договоров:", count)
