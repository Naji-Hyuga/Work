#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
import os
from datetime import datetime as dt
import time
import crm_api as c


class TestFailException(Exception):
    pass


# Уникальная переменная для номера
number = dt.now().strftime("%y"+"%m"+"%d"+"%H"+"%M"+"%S")

# Словарь с переменными использующимися в запросах
context: dict = {
                "contract_id" : "600ab6a1-31d8-5000-0200-ba551d2fb2cc",
                "contract_code" : "",
                "contract_number" : "",
                "report_id" : "",
                "calc_id" : ""
 }


def requestPost(url, json_query, headers):
    r = requests.post(url, data=json.dumps(json_query), headers=headers)
    return r


def requestGet(url, payload, headers):
    r = requests.get(url, params=payload, headers=headers)
    return r


# Авторизация
def authcrm(crm_url, auth_payload, auth_headers):
    auth = requestPost(crm_url, auth_payload, auth_headers)
    token = 'Bearer ' + auth.json()['access_token']
    headers = auth_headers
    headers["authorization"] = token
    # print(token)
    return headers

headers = authcrm(c.auth_url, c.auth_data, c.auth_headers)

# Создание субъекта или объекта
def create(what, data, desc):
    entity = requestPost(what, data, headers)
    if entity.status_code != 200:
        if desc == "mp":
            print("Ошибка создания физ. объекта.")
            print(json.loads(entity.text), "\n")
        elif desc == "trk":
            print("Ошибка создания объекта транслятора.")
            print(json.loads(entity.text), "\n")
        elif desc == "trkr":
            print("Ошибка создания объекта ретранслятора.")
            print(json.loads(entity.text), "\n")
        elif desc == "avp":
            print("Ошибка создания физ. объекта.")
            print(json.loads(entity.text), "\n")
        elif desc == "fil":
            print("Ошибка создания физ. объекта.")
            print(json.loads(entity.text), "\n")
        elif desc == "subject":
            print("Ошибка создания субъекта.")
            print(json.loads(entity.text), "\n")
        elif desc == "event":
            print("Ошибка создания мероприятия.")
            print(json.loads(entity.text), "\n")
    else:
        if desc == "mp":
            print("Объект для мелкой публички создан.")
        elif desc == "trk":
            print("Объект для транслятор создан.")
            return (entity.json()['meta']['object_id'])
        elif desc == "trkr":
            print("Объект для ретранслятор создан.")
            return (entity.json()['meta']['object_id'])
        elif desc == "avp":
            print("Объект для АВП создан.")
        elif desc == "fil":
            print("Объект для филармоний создан.")
        elif desc == "subject":
            print("Субъект создан.")
        elif desc == "event":
            print("Мероприятие создано.")



# Поиск
def find(what, query, desc, t):
    if t == "o":
        query["f[search][eq]"] = desc
    else:
        query["f[search][search]"] = desc
    result = requestGet(what, query, headers)
    if result.status_code != 200:
        print(json.loads(result.text))
    else:
        return (result.json()["data"]["list"][0]["id"])



# Выбор тестовых данных для заданного сервера
if c.server == 'preprod':
    c.preprod_subjects["ru"] = find(c.getsubjlist, c.getsubjlist_query, "ААА Тест Кейс", "s")
    c.preprod_ojects['rate']["id"] = find(c.getobjlist, c.getsubjlist_query, "Бар Хмельной Топаз", "o")
    c.preprod_ojects['trk']["id"] = find(c.getobjlist, c.getobjlist_query, "Транслятор AUtest СМИ", "o")
    c.preprod_ojects['trkr']["id"] = find(c.getobjlist, c.getobjlist_query, "Ретранслятор AUtest СМИ", "o")
    c.preprod_ojects['avp']["id"] = find(c.getobjlist, c.getobjlist_query, "Кинотеатр стрела", "o")
    c.preprod_ojects['fil']["id"] = find(c.getobjlist, c.getobjlist_query, "Дом культуры Смена", "o")
    # c.preprod_ojects['event']["id"] = t.find(c.geteventlist, c.getobjlist_query, "концерт Руки Вверх", "e")
    c.objects = c.preprod_ojects
    c.subjects = c.preprod_subjects
if c.server == 'hotfix':
    c.hotfix_subjects["ru"] = find(c.getsubjlist, c.getsubjlist_query, "ААА Тест Кейс", "s")
    c.hotfix_objects['rate']["id"] = find(c.getobjlist, c.getobjlist_query, "Бар Хмельной Топаз", "o")
    c.hotfix_objects['trk']["id"] = find(c.getobjlist, c.getobjlist_query, "Транслятор AUtest СМИ", "o")
    c.hotfix_objects['trkr']["id"] = find(c.getobjlist, c.getobjlist_query, "Ретранслятор AUtest СМИ", "o")
    c.hotfix_objects['avp']["id"] = find(c.getobjlist, c.getobjlist_query, "Кинотеатр стрела", "o")
    c.hotfix_objects['fil']["id"] = find(c.getobjlist, c.getobjlist_query, "Дом культуры Смена", "o")
    # c.hotfix_objects['event']["id"] = t.find(c.geteventlist, c.getobjlist_query, "концерт Руки Вверх")
    c.objects = c.hotfix_objects
    c.subjects = c.hotfix_subjects
if c.server == 'bel':
    c.subjects = c.bel_subjects
    c.objects = c.bel_objects
if c.server == 'kz':
    c.subjects = c.kz_subjects
    c.objects = c.kz_objects


c.addCont_data["subject_id"] = c.subjects['ru']
c.addRateCond_payload["useobject_id"] = c.objects["rate"]["id"]
c.addPercentcond_data["useobject_id"] = c.objects["trk"]["id"]
c.addEvent_data["event_id"] = c.objects["event"]["id"]
c.mp_report_data["useobject_ids[]"] = c.objects["rate"]["id"]
c.addretransalor_data["translator_id"] = c.objects["trk"]["id"]
c.addretransalor_data["useobject_id"] = c.objects["trkr"]["id"]
c.mpr_report_data["useobject_ids[]"] = c.objects["rate"]["id"]
c.mp_event_data["event_useobject_id"] = c.objects["rate"]["id"]
c.event_report_data["event_id"] = c.objects["event"]["id"]
c.fil_report_data["event_useobject_id"] = c.objects["fil"]["id"]
c.avp_report_data["useobject_ids[]"] = c.objects["avp"]["id"]


# Создание договора
def addContract(category, data):
    data['usecategory_id'] = category
    data["doc_number"] = "AU-" + number
    contract = requestPost(c.addcontract, data, headers)
    if contract.status_code == 200:
        context["contract_id"] = contract.json()['data']['item']['id']
        context["contract_code"] = contract.json()['data']['item']['code']
        context["usecategory_id"] = category
        context["subject_id"] = contract.json()['data']['item']['subject_id']
        context["contract_number"] = contract.json()['data']['item']['doc_number']
        print(f'Создан договор id: {context["contract_id"]}')
    else:
         print(json.loads(contract.text))
         raise SystemExit


# Добавление условия оплаты или ставкки по объекту
def add_commonrate_condition(add_condition_url, condition_data):
    condition_data['contract_id'] = context['contract_id']
    condition_data['reason_id'] = context['contract_id']
    addcomcond = requestPost(add_condition_url, condition_data, headers)
    if addcomcond.status_code != 200:
         print(json.loads(addcomcond.text))
         raise SystemExit


# Перевод договора в действующий
def activate_contract(data):
    edit_contract_data = c.edit_contract_data
    edit_contract_data["doc_number"] = data["contract_number"]
    edit_contract_data["id"] = data["contract_id"]
    edit_contract_data["code"] = data["contract_code"]
    edit_contract_data["usecategory_id"] = data["usecategory_id"]
    edit_contract_data["subject_id"] = data["subject_id"]
    edit_contract_data["status_id"] = c.status["approvment"][0]
    edit_contract_data["status_code"] = c.status["approvment"][1]
    editcontract = requestPost(c.edit_contract_url, edit_contract_data, headers)
    if editcontract.status_code != 200:
        print(json.loads(editcontract.text))
        raise SystemExit
    else:
        edit_contract_data["status_id"] = c.status["confirmed"][0]
        edit_contract_data["status_code"] = c.status["confirmed"][1]
        editcontract = requestPost(c.edit_contract_url, edit_contract_data, headers)
        if editcontract.status_code != 200:
            print(json.loads(editcontract.text))
            raise SystemExit
        else:
            edit_contract_data["status_id"] = c.status["active"][0]
            edit_contract_data["status_code"] = c.status["active"][1]
            editcontract = requestPost(c.edit_contract_url, edit_contract_data, headers)
            if editcontract.status_code != 200:
                print(json.loads(editcontract.text))
                raise SystemExit
            else:
                print("Договор действует.")
                time.sleep(5)


# Идентификация платежа
def ident_payment(context_data, ident_data):
    ident_data["contract_id"] = context_data["contract_id"]
    ident_data["subject_id"] = context_data["subject_id"]
    ident = requestPost(c.ident_add, ident_data, headers)
    if ident.status_code != 200:
        print(json.loads(ident.text))
        raise SystemExit
    else:
        print("Платеж идентифицирован")


# Сопоставление начисления
def calc_execute(context_data, calc_execute_data):
    time.sleep(2)
    getcalculates_query = c.getCalculates_query
    getcalculates_query["contract_id"] = context_data["contract_id"]
    calc = requestGet(c.getCalculates, getcalculates_query, headers)
    if calc.status_code != 200:
        print(json.loads(calc.text))
        raise SystemExit
    try:
        context["calc_id"] = calc.json()["data"]["list"][-1]['grouped_ids'][0]
    except:
        context["calc_id"] = calc.json()["data"]["item"]['grouped_ids'][-1]
    execute_data = calc_execute_data
    execute_data["data"]["calculation_id"] = [context["calc_id"]]
    execute = requestPost(c.calcExecute, execute_data, headers)
    if execute.status_code != 200:
        print(json.loads(execute.text))
        raise SystemExit
    else:
        print("Начисление сопоставлено")

# Частичное сопоставление
def calc_execute2(context_data, calc_execute_data):
    time.sleep(2)
    getcalculates_query = c.getCalculates_query
    getcalculates_query["contract_id"] = context_data["contract_id"]
    calc = requestGet(c.getCalculates, getcalculates_query, headers)
    if calc.status_code != 200:
        print(json.loads(calc.text))
        raise SystemExit
    try:
        context["calc_id"] = calc.json()["data"]["list"][-2]['grouped_ids'][0]
    except:
        context["calc_id"] = calc.json()["data"]["item"]['grouped_ids'][-1]
    execute_data = calc_execute_data
    execute_data["data"]["calculation_id"] = [context["calc_id"]]
    execute_data["data"]["sum"] = 50
    execute = requestPost(c.calcExecute, execute_data, headers)
    if execute.status_code != 200:
        print(json.loads(execute.text))
        raise SystemExit
    else:
        print("Начисление частично сопоставлено")


# Отправка отчета в СРО
def send_report(data):
    print("Отправка отчета в СРО")
    send_report_data = c.send_report_data
    send_report_data["id"] = data
    send_reports = requestPost(c.send_report_url, send_report_data, headers)
    if send_reports.status_code != 200:
        print(json.loads(send_reports.text))
    else:
        print("Отчет успешно отправлен")


# Добавление отчета
def add_report(context_data, report_data):
    rheaders = headers.copy()
    del rheaders["Content-Type"]
    report_data["contract_name"] = context_data["contract_number"]
    report_data["contract_id"] = context_data["contract_id"]
    files = {'report_file[0][file]': open('test.txt', 'rb')}
    report = requests.post(c.add_report_url, data=report_data, headers=rheaders, files=files)
    if report.status_code != 200:
        print(json.loads(report.text))
        raise SystemExit
    context["report_id"] = report.json()["data"]["item"]["id"]
    print(f"Id созданного отчета: {context['report_id']}")


# Создание отчета из ведомости
def add_register(context_data, register_data):
    register_data["contract_id"] = context_data["contract_id"]
    register = requestPost(c.register_add, register_data, headers)
    if register.status_code != 200:
        print(json.loads(register.text))
        raise SystemExit
    context["register_id"] = register.json()["data"]["id"]
    izr_report_data = c.izr_report_data
    izr_report_data["register_id"] = context["register_id"]
    izr = requestPost(c.izr_report, izr_report_data, headers)
    if register.status_code != 200:
        print(json.loads(izr.text))
        raise SystemExit
    context["izr_id"] = izr.json()["data"]["id"]
    izr_file_data = c.izr_file_data
    izr_file_data["id"] = context["izr_id"]
    rheaders = headers.copy()
    del rheaders["Content-Type"]
    files = {'file' : open('test.txt', 'rb')}
    izr_file = requests.post(c.izr_file, data=izr_file_data, headers=rheaders, files=files)
    if izr_file.status_code != 200:
        print(json.loads(izr_file.text))
        raise SystemExit
    context["virtual_id"] = izr_file.json()['data']['virtual_id']
    izr_edit_data = c.izr_edit_data
    izr_edit_data["id"] = context["virtual_id"]
    izr_edit = requestPost(c.izr_edit, izr_edit_data, headers)
    if izr_edit.status_code != 200:
        print(json.loads(izr_edit.text))
        raise SystemExit
    izr_payment_data = c.izr_payment_data
    izr_payment_data['register_id'] = context["register_id"]
    izr_payment = requestPost(c.izr_payment, izr_payment_data, headers)
    if izr_payment.status_code != 200:
        print(json.loads(izr_payment.text))
        raise SystemExit
    izr_getpayments_data = c.izr_getpayments_params
    izr_getpayments_data["register_id"] = context["register_id"]
    izr_getpayments_data["subject_id"] = c.subjects['sw']
    izr_getpayments = requestPost(c.izr_getpayments, izr_getpayments_data, headers)
    if izr_getpayments.status_code != 200:
        print(json.loads(izr_getpayments.text))
        raise SystemExit
    register_submit_data = c.register_submit_data
    register_submit_data['id'] = context["register_id"]
    izr_submit = requestPost(c.register_submit, register_submit_data, headers)
    if izr_submit.status_code != 200:
        print(json.loads(izr_submit.text))
        raise SystemExit
    print("Ведомость создана")
    print(json.loads(izr_edit.text))


# Загрузка платежей из ексель
def load_payment(payment_data, files):
    rheaders = headers.copy()
    del rheaders["Content-Type"]
    load = requests.post(c.load_payment_url, data=payment_data, headers=rheaders, files=files)
    # if load.status_code != 200:
    print(json.loads(load.text))



# Проверка пользователя в фонмикс
def fonmix_check(subject, headers):
    check = requestPost(c.chekSubject, subject, headers)
    if check.json()['success'] == 1:
        crm = check.json()['data']['exists_crm']
        crm_id = check.json()['data']['subjects'][0]['id']
        dadata = check.json()['data']['exists_dadata']
        dadata_data = check.json()['data']['dadata'][0]['value']
        # print(json.loads(check.text))
        print(f" Наличие в црм: {crm} \n CRM id: {crm_id} \n Наличие в dadata: {dadata} \n Данные в dadata: {dadata_data}")
    else:
        print(json.loads(check.text))



# Создание тестовых данных
if __name__ == "__main__":
    create(c.addsubject, c.addsubject_data2, "subject")
    create(c.addobject, c.addobjectmp_data, "mp")
    trans = create(c.addobject, c.addobjecttrk_data, "trk")
    c.addretransalor_data["translator_id"] = trans
    retrans = create(c.addobject, c.addobjecttrk_r_data, "trkr")
    c.addretransalor_data["useobject_id"] = retrans
    requestPost(c.addretranslator_url, c.addretransalor_data, headers)
    create(c.addobject, c.addobjectavp_data, "avp")
    create(c.addobject, c.addobjectfil_data, "fil")
    # create(c.create_event, c.create_event_data, "event")
    print("Создание данных завершено")
