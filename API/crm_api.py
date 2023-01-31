#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


server = "preprod"
if os.getenv('preprod'):
    server = "preprod"
if os.getenv('hotfix'):
    server = "hotfix"
if os.getenv('kgz'):
    server = "kgz"
if os.getenv('bel'):
    server = "bel"


if server == "preprod":
    url = "https://crm-preprod.k8s.id-network.ru"
    payment = "5e19e021-8cae-1000-0140-4b026c540e8a"
    ogrn = "1186196043340"
    fm_id = "3"
    sysowner = "00000000-0000-0000-0002-000000000002"
    department_id = "5af15183-06aa-1900-0025-ca4dd5350d32"
    cont_type_id = 5
elif server == 'hotfix':
    url = "https://crm-hotfix.k8s.id-network.ru"
    payment = "5e19e021-8cae-1000-0140-4b026c540e8a"
    ogrn = "1186196043340"
    fm_id = "3"
    sysowner = "00000000-0000-0000-0002-000000000002"
    department_id = "5af15183-06aa-1900-0025-ca4dd5350d32"
    cont_type_id = 5
elif server == "bel":
    url = "https://crm-blr-preprod.dev.k8s.id-network.ru"
    payment = "5fdca842-c70b-c000-0140-363f57a0addf"
    ogrn = "1035010951502"
    fm_id = "267"
    sysowner = "00000000-0000-0000-0002-000000030001"
    department_id = "5f75e706-5cb1-5000-0025-d202ec795356"
    cont_type_id = 1
elif server == "kz":
    url = "https://crm.hypergraph.kz/"
    payment = "5dc2c38f-ac99-1000-0140-72e8c59f81f9"
    sysowner = "00000000-0000-0000-0002-000000010001"
    department_id = "5db9929e-4309-d000-0025-7fc829fac580"
    cont_type_id = 1
    fm_id = 5
    # 'password': 'usercrm435'
elif server == "PROD":
    url = "https://crm.id-network.ru/"
    payment = ""
    ogrn = "1186196043340"
    fm_id = "3"
    sysowner = "00000000-0000-0000-0002-000000000003"
    department_id = "5af15183-06aa-1900-0025-ca4dd5350d32"
    cont_type_id = 5
else:
    url = "https://crm-test.k8s.id-network.ru"
    payment = "5d1cd1a7-b0b9-5000-0140-5207f36f8a9f" # РАО
    # payment = "5e849511-c50b-0000-0140-dbdb64130766" # для формакс
    ogrn = "1035010951502"
    fm_id = "267"
    sysowner = "00000000-0000-0000-0002-000000000002"
    department_id = "5af15183-06aa-1900-0025-ca4dd5350d32"
    cont_type_id = 5


# Даты начала действия договров и ставок
period = {"beg" : "2022-01-01", "end" : "2022-12-31"}


# Субъекты использующиеся в договорах
subjects = {"ru" : "6241d6b4-c773-3000-0100-bcc4a17e9c66", "sw" : "5ebbce1f-77de-5000-0100-620740edada9"}

preprod_subjects = {"ru" : "", "sw" : "5e063821-76c5-b000-0100-c60effcaf1fa"}

hotfix_subjects = {"ru" : "", "sw" : "5e063821-76c5-b000-0100-c60effcaf1fa"}

bel_subjects = {'ru' : '60099078-5612-7000-0100-2e88a94f598b'}

kz_subjects = {'ru' : '5dbc1340-1fec-0000-0100-2035b3c840b7'}


# Объекты использующиеся в договорах
objects = {
            "rate" : {"id" : "5d10a033-a651-b000-0110-7aa517806040", "name": "Бар Хмельной Топаз"},
            "trk" : {"id" : "5f76f46d-4fa9-2000-0110-956caf525c76", "name": "Транслятор AUtest СМИ"},
            "trkr" : {"id" : "5f76f46e-a218-6000-0110-761bc0d6ece6", "name" : "Ретранслятор AUtest СМИ"},
            "event" : {"id" : "5e26fcad-c3b9-1000-0300-f47425224ca3", "name": "концерт Руки Вверх"},
            "avp" : {"id" : "5ea96a97-c9d4-b000-0110-d71ddae55da7", "name": "Кинотеатр стрела"},
            "fil" : {"id" : "5ea99c53-1b43-5000-0110-bb9011dadaff", "name": 'Дом культуры Смена'}
            }

preprod_ojects = {
                "rate" : {"id" : "", "name": "Бар Хмельной Топаз"},
                "trk" : {"id" : "", "name": "Транслятор AUtest СМИ"},
                "trkr" : {"id" : "", "name" : "Ретранслятор AUtest СМИ"},
                "event" : {"id" : "", "name": "концерт Руки Вверх"},
                "avp" : {"id" : "", "name": "Кинотеатр стрела"},
                "fil" : {"id" : "", "name": 'Дом культуры Смена'}
                }

hotfix_objects = {
                "rate" : {"id" : "", "name": "Бар Хмельной Топаз"},
                "trk" : {"id" : "", "name": "Транслятор AUtest СМИ"},
                "trkr" : {"id" : "", "name" : "Ретранслятор AUtest СМИ"},
                "event" : {"id" : "", "name": "концерт Руки Вверх"},
                "avp" : {"id" : "", "name": "Кинотеатр стрела"},
                "fil" : {"id" : "", "name": 'Дом культуры Смена'}
                }

bel_objects = {
    "rate" : {"id" : "60094d53-032f-c000-0110-784067de8cc7", "name": "Бар Хмельной Топаз"},
    "trk" : {"id" : "5fe07c07-b2bd-0000-0110-dfbfebe848ae", "name": "Транслятор AUtest СМИ"},
    "trkr" : {"id" : "5fe07c89-a23b-5000-0110-de4bca106f5d", "name" : "Ретранслятор AUtest СМИ"},
    "event" : {"id" : "", "name": "концерт Руки Вверх"},
    "avp" : {"id" : "", "name": "Кинотеатр стрела"},
    "fil" : {"id" : "", "name": 'Дом культуры Смена'}
}

kz_objects = {
    "rate" : {"id" : "60b4de98-65c1-7000-0110-81f10b1eb615", "name": "Бар Хмельной Топаз"},
    "trk" : {"id" : "60b4de99-c694-d000-0110-424b2c72dcac", "name": "Транслятор AUtest СМИ"},
    "trkr" : {"id" : "60b4de99-26bf-3000-0110-27cb6968c348", "name" : "Ретранслятор AUtest СМИ"},
    "event" : {"id" : "", "name": "концерт Руки Вверх"},
    "avp" : {"id" : "", "name": "Кинотеатр стрела"},
    "fil" : {"id" : "60b4de9a-6951-9000-0110-88b8b8052ae7", "name": 'Дом культуры Смена'}
}

# Authorization
auth_url = url + "/api/oauth/token"

auth_data = {'username': 'crmuser@test.api', 'password': 'user123', 'grant_type': 'password'}
if server == "PROD":
    auth_data['password'] = 'usercrm987'

auth_headers = {"Accept": "application/json, text/plain, */*",
                 "Content-Type": "application/json",
                 "x-project-name": "crm",
                 "x-sysowner-id": sysowner,
                #  "X-Secret-Key" : "C0de69da1f5FFa7e68F05ECC6B3D9C46"
                 }


# Contracts
getcontList = url + "/api/contract/list"
getcontList_payload = {"f[status_id][in][]": "5aea9486-06b5-4200-0020-9b3d2a9c90e4",
                    "with": ["department", "status", "subject", "usecategory", "actual_roles", "executor"],
                    "f[is_main][eq]": "true"}
status = {
        "project" : "5abd020c-03d8-2700-0020-30bac9021aaa",
        "approvment" : ["5abd0415-0e5b-c300-0020-638c65450acf", 3],
        "rework" : "5e19bad6-9be5-2000-0100-d34a5d48ffe9",
        "confirmed" : ["5abd0415-0e5b-c300-0020-638c65450ace", 4],
        "active" : ["5aea9486-06b5-4200-0020-9b3d2a9c90e4", 10],
        "closed" : "5aea94b6-0312-4400-0020-838dfca3ff00",
        "archive" : "5aea94de-098c-da00-0020-e77659ac8254",
        "bin" : "5af99aae-097d-8700-0020-0c444dc1b39f",
        "deleted" : "5e67bb33-07d2-6000-0020-d340f7db4fd1"
        }

category = {
            "mp" : "5abe2e68-002c-c000-0024-883d02f16496",
            "avp" : "5abe2e68-002e-2600-0024-d00e13cff8d0",
            "event" : "5abe2e68-002c-5800-0024-4e334b2a9c13",
            "trk" : "5dfc7f82-2817-5000-0024-39301bc40e67",
            "fil" : "5abe2e68-002c-9300-0024-722a10854bb7",
            "izr" : "5cdea887-9c7a-2000-0024-e491ce19dafe"}

category_bel = {"mp" : "5fda247c-af87-0000-0024-3c5859904a47",
                "trk" : "5fda247c-af87-0000-0024-0ae0951f2a98"}

category_kz = {'mp' : "5abe2e68-002c-c000-0024-883d02f16496",
                "trk" : "5abe2e68-002e-6100-0024-00826bc956a7"}
if server == 'bel':
    category = category_bel
elif server == 'kz':
    category = category_kz

# Создание договора
addcontract = url + "/api/contract/add"
addCont_data = {"id": None,
                "doc_number": "",   # Номер договора
                "type_id": cont_type_id, # ru 5 bel 1
                "sysowner_id": sysowner,
                "status_id": "5abd020c-03d8-2700-0020-30bac9021aaa",
                "subject_id": "",   # id субъекта
                "doc_date": period["beg"],
                "date_beg": period["beg"],
                "date_end": period["end"],
                "department_id": department_id,
                "department_child_ids": "",
                "usecategory_id": "",
                "brandObject": "",
                "brand_id": None,
                "status": None,
                "returning": True
                   }





# Добавление условия оплаты и отчетов
addComCond = url + "/api/contract/condition/common/add"
addComCond_payload = {"pay_period_id": "5ae16388-02c5-f000-0020-ff478484dfed",  # Месяц
                    "pay_term_day": "5",
                    "pay_fine_kind": 2,
                    "pay_fine_value": 0.1,
                    "report_fine_kind": 1,
                    "report_fine_value": 100,
                    "report_period_id": "5ae16388-02c5-f000-0020-ff478484dfed", # Месяц
                    "report_term_day": "5",
                    # "report_form_id": "5aeac159-0a0f-3b00-0020-8c12652217fb",   # На бумажном носителе
                    # "report_address_to": "test",
                    "fonmix_activation": False,
                    "date_beg": period["beg"],
                    "contract_id": "",  # id договора
                    "reason_id": "",    # id договора
                   }

# Добавление ставки по объекту фикс
addRateCond = url + "/api/contract/condition/rate/add"
addRateCond_payload = {"id": None,
                        "contract_id": "",  # Id договора
                        "reason_id": "",    # Id договора
                        "display_name": None,
                        "date_beg": None,
                        "date_end": None,
                        "notes": "",
                        "type": "rate",
                        "systype": 2,
                        "subtype_id": 11,
                        "is_percent": False,
                        "useobject_id": "", # id объекта
                        "usecategory_id": category['mp'],
                        "rate_values": [{
                                        "id": None,
                                        "condition_id": None,
                                        "sysowner_id": sysowner,
                                        "date_beg": period["beg"],
                                        "date_end": None,
                                        "season_date_beg": None,
                                        "season_date_end": None,
                                        "sum": 100,
                                        "percent": "",
                                        "min_sum": "",
                                        "actual_date_beg": None,
                                        "actual_date_end": None,
                                        "prev_id": None,
                                        "action": 1,
                                        "kind": 1,
                                        "vat_rate": 0,
                                        }]
                    }

# Добавление ставки по объекту процент
addPercentcond_data = {
                        "id": None,
                        "contract_id": "",   # Id договора
                        "reason_id": "",    # Id договора
                        "display_name": None,
                        "date_beg": None,
                        "date_end": None,
                        "notes": None,
                        "systype": 2,
                        "subtype_id": 12,
                        "is_percent": True,
                        "useobject_id": "", # ID объекта
                        "usecategory_id": category['trk'],
                        "rate_values": [{
                                        "id": None,
                                        "condition_id": None,
                                        "sysowner_id": sysowner,
                                        "date_beg": period["beg"],
                                        "date_end": None,
                                        "season_date_beg": None,
                                        "season_date_end": None,
                                        "sum": None,
                                        "percent": 10,
                                        "min_sum": 100,
                                        "actual_date_beg": None,
                                        "actual_date_end": None,
                                        "prev_id": None,
                                        "action": 1,
                                        "kind": 1,
                                        "vat_rate": 0
                                        }]
                        }

# Добавление условия мероприятия
addEvent_url = url + "/api/contract/condition/event/add"
addEvent_data = {
                "event_id": "",
                "reason_id": "",
                "contract_id": "",
                "type": 1
                }

# Генерация номера
conGenNum = url + "/api/contract/generate_number"
conGenNum_data = {"contract_id": ""}

# Редактирование договора
edit_contract_url = url + "/api/contract/edit"
edit_contract_data = {"id": "", # id договора
                    "type_id": cont_type_id, # RU 3 bel 1
                    "sysowner_id": sysowner,
                    "status_id": "5abd0415-0e5b-c300-0020-638c65450acf",  # Проект согласование
                    "status_code": 3, # Код статуса обязательное поле
                    "subject_id": "",
                    "parent_id": None,
                    "name": "Основание не указано",
                    "doc_number": "", # Номер договора
                    "doc_date": period["beg"],
                    "date_beg": period["beg"],
                    "date_end": period["end"],
                    "date_close": None,
                    "department_id": department_id,
                    "department_child_ids": None,
                    "usecategory_id": "", # Категория договора
                    "brandObject": [],
                    "brand_id": None,
                    "auto_prolongation": None,
                    "notes": None,
                    "code": "", # Код договора
                    "is_main": True,
                    "executor_id": "5cffbc07-ba0d-a000-0040-b97a00782e14",
                    "json_custom": None,
                    "tarif_sum": 0,
                    "tarif_percent": None,
                    "tarif_is_calculated": True,
                    "flags": [1],
                    "dop_cnt": None,
                    "dop_cnt_project": None,
                    "useobject_cnt": None,
                    "useobject_usecategory_ids": None,
                    "doc_dop_number": None,
                    "parent_date_end": None,
                    "parent_auto_prolongation": None,
                    "migrate_date": None,
                    "sum_receivables": 0,
                    "pay_fine": 0,
                    "report_fine": 0,
                    "useobject_active_count": 0,
                    "contract_rate_sum": 0,
                    "useobject_usecategory_details": None,
                    "useobjects": [],
                    "parent": None,
                    "brand": None,
                    "calculations": [],
                    "common_conditions": [],
                    "actual_roles": [],
                    "returning": True}


# Субъекты
getsubjlist = url + "/api/subject/list"
getsubjlist_query = {
                    "f[search][search]": "Нарсис",
                    "p[count]": 50, "p[total]": 1, "p[page]": 1, "p[limit]": 50,
                    "with": "type_classifier, status_classifier, names, documents"
                    }
# Создание субъекта
addsubject = url + "/api/subject/add"
addsubject_data = {
                    "address": "Вивек",
                    "country_code": "RUS",
                    "documents": [{"kind": "1", "doc_series": "4218", "doc_number": "447821"},
                                  {"kind": "4", "regnum1": "399650073551"},
                                  {"kind": "8", "regnum1": "242-912-231-43"}],
                    "json_custom": {"date_b": "11.04.1985"},
                    "names": [{"kind": "1", "name": "Нарсис Дрен"},
                              {"kind": "4", "name": "Дрен"},
                              {"kind": "5", "name": "Нарсис"},
                              {"kind": "6"}],
                    "type": "1"
                    }

addsubjectbel_data = {
                    "address": "Вивек",
                    "country_code": "BLR",
                    "documents": [{"kind": "31", "regnum1": "МА1953684"},
                                  {"kind": "33", "regnum1": "4110873B058PB8"}],
                    "json_custom": {"date_b": "11.04.1985"},
                    "names": [{"kind": "1", "name": "Нарсис Дрен"},
                              {"kind": "4", "name": "Дрен"},
                              {"kind": "5", "name": "Нарсис"},
                              {"kind": "6"}],
                    "type": "1"
                    }

addsubject_data2 = {
"address": "г Москва, ул Новослободская, д 75 стр 1",
"country_code": "RUS",
"documents": [
    {"kind": "5", "regnum1": "6545501687", "regnum2": "419844420"},
    {"kind": "7", "regnum1": "1148724192891"}
    ],
"names": [
    {"kind": "1", "name": "ААА Тест Кейс"},
    {"kind": "2", "name": "ААА Тест Кейс"},
    {"kind": "3", "name": "АТК"}
    ],
"type": "2"
}

# Объекты
getobjlist = url + "/api/useobject/list"
geteventlist = url + "/api/event/list"
getobjlist_query = {
                    "f[search][eq]": "Бар Хмельной Топаз",
                    "p[count]": 1,
                    "p[total]": 1,
                    "p[page]": 1,
                    "p[limit]": 50,
                    "with": "all"
                    }
# Создание объекта
addobject = url + "/api/useobject/add"
# Бар для мелкой публички
addobjectmp_data = {
                "address": "г Москва, поселение Десеновское, Нововатутинский пр-кт, д 65",
                "address_element_id": "413a78c6-d1f2-46a2-b9bb-e95778266bbf",
                "address_json": {
                            "value": "г Москва, поселение Десеновское, Нововатутинский пр-кт, д 65",
                            "unrestricted_value": "108818, г Москва, поселение Десеновское, Новомосковский округ, Нововатутинский пр-кт, д 65",
                            "data": {"postal_code": "108818", "country": "Россия", "country_iso_code": "RU"}
                                },
                "address_postcode": "108818",
                "name": "Бар Хмельной Топаз",
                "type_id": 1
                }

# СМИ для ТРК
addobjecttrk_data = {
                    "address_json": None,
                    "lic_date_beg": "01.11.2018",
                    "lic_date_end": "31.12.2023",
                    "lic_number": "au",
                    "lic_percent_music": 70,
                    "lic_territory": "Российская федерация",
                    "lic_volume": 48,
                    "name": "Транслятор AUtest СМИ",
                    "place_name": "ФЫВ",
                    "type_id": 2,
                    "is_translator": True
                    }

# Создание объекта ретранслятора
addobjecttrk_r_data = {
                    "address_json": None,
                    "lic_date_beg": "01.11.2018",
                    "lic_date_end": "31.12.2023",
                    "lic_number": "au",
                    "lic_percent_music": 70,
                    "lic_territory": "Российская федерация",
                    "lic_volume": 48,
                    "name": "Ретранслятор AUtest СМИ",
                    "place_name": "ФЫВ",
                    "type_id": 2,
                    "is_translator": False
                    }

addretranslator_url = url + "/api/useobject/retranslation/add"
addretransalor_data = {
                        "returning": True,
                        "translator_id": "", # ID объекта транслятора
                        "useobject_id": "",  # ID объекта
                        "volume": 24
                    }


# Кинотеатр для АВП
addobjectavp_data = {
                    "address": "г Москва, ул Смоленская",
                    "address_element_id": "773c3328-dfeb-46d1-9ad5-bb38d4fd5301",
                    "address_json": {
                                "data": {"postal_code": None, "country": "Россия", "country_iso_code": "RU"},
                                "unrestricted_value": "г Москва, ул Смоленская",
                                "value": "г Москва, ул Смоленская"
                                    },
                    "address_postcode": None,
                    "name": "Кинотеатр стрела",
                    "type_id": 1
                    }

# Дом культуры для филармонии
addobjectfil_data = {
                    "address": "г Москва, ул Корнейчука",
                    "address_element_id": "6d86b556-48a3-4d0d-ad54-5bcd450ee502",
                    "address_json": {
                                    "data": {"postal_code": "127543", "country": "Россия", "country_iso_code": "RU"},
                                    "unrestricted_value": "127543, г Москва, ул Корнейчука",
                                    "value": "г Москва, ул Корнейчука"
                                    },
                    "address_postcode": "127543",
                    "name": 'Дом культуры Смена',
                    "type_id": 1
                    }

# Мероприятие
create_event = url + "/api/event/add"
create_event_data = {
                "address": "Москва ленинградское шоссе д. 64",
                "date_beg": "2020-01-30",
                "date_end": "2020-01-30",
                "kind_id": "5bd2bcc7-075e-b000-002a-b6c844fbe849",
                "name": "концерт Руки Вверх",
                "params": [],
                "performers": [{"fullname": "Руки вверх"}],
                "prefabricated": False,
                "territory_name": "f",
                "type": 1
                }


# Payments
ident_add = url + "/api/payment/ident_variant/add"
identAdd_data = {
                "contract_id": "",   # id договора
                "origin_id": "5ad6f22c-0cd5-d700-0020-7b97156f8347",
                "payment_id": payment,   # id платежа
                "subject_id": ""    # id субъекта
                }
identDelete = url + "/api/payment/ident_variant/delete"
identDelete_payload = {"id": payment} # ID платежа

# Радота с начислениями
getCalculates = url + "/api/calculation/contract_calculation" # Получение списка начислений
getCalculates_query = {
                        "contract_id": "",
                        "not_compared_only": True,
                        "group_by_type": 1
                            }

calcExecute = url + "/api/finhub/operation/execute" # Сопоставление начисления
calcExecute_data = {
                    "type": 1,
                    "data" : {
                                "payment_id": payment,   # id платежа
                                "sum": 100,
                                "calculation_id": [""]
                                },

                    }


# Создание отчета
add_report_url = url + "/api/report/add"
# Мелкая публичка
mp_report_data = {
                    "type": 1,
                    "contract_name": "", # номер договора
                    "contract_id": "",
                    "period_date_beg": "2022-01-01",
                    "period_date_end": "2022-01-31",
                    "report_date": "2022-04-01",
                    "sum_report": 100,
                    "usecategory_id": "5abe2e68-002c-c000-0024-883d02f16496",
                    "useobject_ids[]": [], # ID объекта
                    "on_rating": 0,
                    "on_fixed_sum": 0,
                    "returning": True,
                    "report_file": [{}],
                    "status": 1,
                    "rate_type_id": 1
                    }

# ТРК  5dd28e10-1ccd-d000-0110-e966685b28fe
trk_report_data = {
                    "type": "4",
                    "status": 1,
                    "rate_type_id": 2,
                    "contract_name": "",    # номер договора
                    "contract_id": "",  # id договора
                    "period_date_beg": "2022-05-01",
                    "period_date_end": "2022-05-31",
                    "report_date": "2022-03-31",
                    "sum_report": "100",
                    "usecategory_id": "5dfc7f82-2817-5000-0024-39301bc40e67",
                    "sum_income": "1000",
                    "rate": "10",
                    "sum_estimated": "100",
                    "useobject_ids[]": [],  # ID объекта
                    "on_rating": "0",
                    "on_fixed_sum": "0",
                    "returning": "true",
                    "report_file": [{"title" : "file_1", "id" : None, "useobject_id" : "", "file" : {}}],
                    "useobject_percents" : '' # Данные об объекте
}


# Рспределение без отчета
mpr_report_data = {
                    "contract_id": "",  # id договора
                    "contract_name": "",    # Номер договора
                    "on_fixed_sum": "0",
                    "on_rating": "1",
                    "on_rating_comments": "autotest",
                    "period_date_beg": "2022-01-01",
                    "period_date_end": "2022-01-31",
                    "report_date": "2022-04-01",
                    "returning": "true",
                    "sum_report": "100",
                    "type": "1",
                    "usecategory_id": "5abe2e68-002c-c000-0024-883d02f16496",
                    "useobject_ids[]": []    # ID объекта
                    }


# Мероприятие мелкая публичка
mp_event_data = {
                "address": "г Москва, Нововатутинский пр-кт, д 65",
                "address_json": {'value':'г Москва, поселение Десеновское, Нововатутинский пр-кт, д 65','unrestricted_value':'г Москва, поселение Десеновское, Новомосковский округ, Нововатутинский пр-кт, д 65','data':{'postal_code':'108818','country':'Россия','federal_district':'Центральный','region_fias_id':'0c5b2444-70a0-4932-980c-b4dc0d3f02b5'}},
                "contract_id": "",  # id договора
                "contract_name": "",    # Номер договора
                "event_name": "квиз",
                "event_territory_name": "Бар Хмельной Топаз",
                "event_type_id": "5bd2bcc7-075e-b000-002a-c48177383a52",
                "event_useobject_id": "",   # id объекта
                "on_fixed_sum": "0",
                "on_rating": "0",
                "period_date_beg": "2022-01-01",
                "period_date_end": "2022-01-31",
                "rate": "10",
                "report_date": "2022-04-01",
                "report_file": [{}],
                "returning": "true",
                "sum_estimated": "100",
                "sum_income": "1000",
                "sum_report": "100",
                "type": "5",
                "usecategory_id": "5abe2e68-002c-c000-0024-883d02f16496"
                }


# Мероприятие
event_report_data = {
                    "type": "2",
                    "contract_name": "", # номер договора
                    "contract_id": "",   # id договора
                    "period_date_beg": "2022-01-30",
                    "period_date_end": "2022-01-30",
                    "report_date": "2022-04-01",
                    "sum_report": "100",
                    "usecategory_id": "5abe2e68-002c-5800-0024-4e334b2a9c13",
                    "sum_income": "1000",
                    "rate": "10",
                    "sum_estimated": "100",
                    "event_id": "", # id мероприятия
                    "event_name": "концерт Руки Вверх",
                    "event_category_id": "5bd2bcc7-075e-b000-002a-b6c844fbe849",
                    "event_category": "Концерт",
                    "event_territory_name": "f",
                    "event_type": "Концерт",
                    "event_type_id": "5bd2bcc7-075e-b000-002a-b6c844fbe849",
                    "event_free_entry": "0",
                    "event_not_guarded": "0",
                    "address": "Москва ленинградское шоссе д. 64",
                    "address_json": "null",
                    "on_rating": "0",
                    "on_fixed_sum": "0",
                    "returning": "true",
                    "report_file": [{}]
                    }

# Филармонии
fil_report_data = {
                    "address": "г Москва, ул Корнейчука",
                    "contract_id": "",  # id договора
                    "contract_name": "",  # Номер договора
                    "event_free_entry": "0",
                    "event_name": "вечеринка",
                    "event_type_id": "5bd2bcc7-075e-b000-002a-66f7e87f82ef",
                    "event_not_guarded": "0",
                    "event_territory_name": 'Дом культуры Смена',
                    "event_useobject_id": "",   # id объекта
                    "prefabricated": "1",
                    "on_fixed_sum": "0",
                    "on_rating": "0",
                    "period_date_beg": "2020-01-01",
                    "period_date_end": "2020-01-31",
                    "rate": "10.00",
                    "report_date": "2020-04-01",
                    "report_file": [{}],
                    "returning": "true",
                    "sum_estimated": "100",
                    "sum_income": "1000",
                    "sum_report": "100",
                    "type": "7",
                    "usecategory_id": "5abe2e68-002c-9300-0024-722a10854bb7"
                    }

# АВП
avp_report_data = {
                    "contract_id": "",  # id договора
                    "contract_name": "", # Номер договора
                    "on_fixed_sum": "0",
                    "on_rating": "0",
                    "period_date_beg": "2022-01-01",
                    "period_date_end": "2022-02-29",
                    "rate": "10",
                    "report_date": "2022-04-01",
                    "report_file": [{}],
                    "returning": "true",
                    "sum_estimated": "100",
                    "sum_income": "1000",
                    "sum_report": "100",
                    "type": "3",
                    "usecategory_id": "5abe2e68-002e-2600-0024-d00e13cff8d0",
                    "useobject_ids[]": [""] # id объекта
                    }


# Ведомости
register_add = url + "/api/register/add"
register_data = {
                "contract_id": "",   # id договора
                "country": "Россия",
                "currency": "USD",
                "currency_sum": 100,
                "doc_date": "01.03.2022",
                "period_date_beg": "01.03.2022",
                "period_date_end": "31.03.2022",
                "returning": True,
                "subject": "STIM 079"   # Название субъекта
                }

register_edit = url + "/api/register/edit"

register_submit = url + "/api/register/submit"
register_submit_data = {"id" : 25   # id ведомости
                        }

izr_payment = url + "/api/register/payment/cud"
izr_payment_data = {"payment_id": payment,
                    "register_id": 50,  # id ведомости
                    "sum": 100
                    }

izr_report = url + "/api/register/report/add"
izr_report_data = {
                    "register_id": 37,  # id ведомости
                    "type_id": 6,
                    "usecategory_id": "5dd4f92e-3c08-8000-0024-1f00011bf61d"
                    }


izr_file = url + "/api/register/report/upload"
izr_file_data = {"file": {},
                "id": "",   # id отчета
                "title": "test.txt"
                }

izr_edit = url + "/api/files/edit"
izr_edit_data = {
                "id": "",   # virtual_id
                "json_custom": {"currency": None, "sum_report": 100}
                }

izr_getpayments = url + "/api/register/payment/get_payments"
izr_getpayments_params = {
                        "register_id": 37,  # id ведомости
                        "subject_id": ""    # id субъекта
                        }


# Уведомления по отчетам
notice_url = url + "/api/external/sro/receive_report"   # ACRM-1261
    # Для выполнения этого запроса требуется отдельный токен авторизации
notice_data = {"id": "5e6a47f0-1bc7-a000-0400-c6c965f4a7af",
                  "status": 5,
                  "meassage": "Возврат на доработку. TEST"
}


# Отправка отчетов
send_report_url = url + "/api/report/send_report_sro"
send_report_data = {"id": "5f6893a7-1c17-9000-0400-bef7d746e3d2"}  # ID отчета


#Закгрузка платежей из ексель
load_payment_url = url + "/api/payment/import/excel"
load_payment_data = {
                    "title" : "rao_pay_test.xlsx",
                    "file" : {},
                    }

# Проверка пользователя для фонмикс
    # авторизация для фомикс
fmauth_data = {
                    "grant_type": "client_credentials",
                    "client_id": fm_id, # test 267, hotfix 3, preprod 3
                    "client_secret": "i71Nzo57udXrjvv4ikCgcxfXglLptQ6nzCiekj1g"
                    }

chekSubject = url + "/api/external/fonmix/check/subject"
chekSubject_data = {
                        "ogrn": "1035010951502" # required
                        }


# Создание договора фонмикс
fm_addcontract = url + "/api/external/fonmix/contract/add"
fm_editcontract = url + "/api/external/fonmix/contract/edit"

new = {
        "id": None,
        "subject_type": 2,
        "country": "RUS",
        "short_name": "Shortname",
        "full_name": "Fullname",
        "inn": "1121028901",
        "kpp": "155444769",
        "ogrn": "1221100001319",
        "address": "Moscow",
        "phone_number": "88005553554",
        "email": "mail@example.com",
        "employee": {
            "full_name": "FamilyName",
            "position": "agent",
            "phone_number": "79005551122",
            "email": "employee@example.com",
            "date_beg": "2020-01-01" }
        # "employee": {
        #     "full_name": None,
        #     "position": None,
        #     "phone_number": None,
        #     "email": None,
        #     "date_beg": None
            # }
        }


exist = {"id" : subjects['ru']}

fm_addcontract_data = {
    "contract_type": 14,
    "region": 77,
    "regional_center" : "5af15183-06aa-1900-0025-ca4dd5350d32",
    "doc_date": "2022-07-01",
    # "doc_date_beg" : "2022-03-15",
    "category_id": "5abe2e68-002c-c000-0024-883d02f16496",
    "auto_prolongation": False,
    "executor" : 9194,
    "subject": exist,
    "conditions": {
        "package": "base",
        "validity": 3,
        "validity_type": 1,
        "service": {
            "sum": 100,
            "vat_rate": 20
        },
        "rates": [
            {
                "object_name": "coffe",
                "object_type": 1,
                "object_area": 15,
                "category_fm_id": "101",
                "address": "г. Москва, ул. Большая Якиманка, 22",
                "city": "1827",
                "usecategory_id": "5abe2e68-002c-c000-0024-883d02f16496",
                "rate_type" : 11,
                "sums": [
                    {
                        # "type" : "service",
                        "sys": "rao",
                        "sum": 100.0,
                        "vat_rate": 0,
                    },
                    {
                        # "type" : "service",
                        "sys": "vois",
                        "sum": 100.0,
                        "vat_rate": 0,
                    }
                ]
            }
            # {
            #     "object_name": "hotel",
            #     "object_type": 1,
            #     "address": "Moscow",
            #     "usecategory_id": "5abe2e68-002c-c000-0024-883d02f16496",
            #     "sums": [
            #         {
            #             "sys": "rao",
            #             "sum": 90.0,
            #             "vat_rate": 20
            #         },
            #         {
            #             "sys": "vois",
            #             "sum": 90.0,
            #             "vat_rate": 0
            #         }
            #      ]
            # }
        ]
    },
    "callback_url": "http://example.com/callback",
    "meta" : "test"
}


fm_addcontract_data2 = {
    "contract_type": 15,
    "region": 2,
    # "regional_center": "5af1756f-0eb8-8300-0025-158713baf0c9",
    "doc_date": "2022-09-15",
    # "doc_date_beg" : "2022-03-15",
    "category_id": "5abe2e68-002c-c000-0024-883d02f16496",
    "auto_prolongation": True,
    "executor" : 1163,
    "subject": exist,
    "conditions": {
        "package": "lite",
        "validity": 30,
        "validity_type": 2,
        "service": {
            "sum": 0,
            "vat_rate": 20
        },
        "rates": [
            {
                "object_name": "cyyffe",
                "object_type": 1,
                "object_area": 15,
                "category_fm_id": "101",
                "address": "г. Москва, ул. Большая Якиманка, 22",
                "city": "1827",
                "usecategory_id": "5abe2e68-002c-c000-0024-883d02f16496",
                "rate_type" : 13,
                "sums": [
                    # {
                    #     "type" : "base_rate",
                    #     "sys": "rao",
                    #     "sum": 100,
                    #     "vat_rate": 0
                    # },
                    # {
                    #     "type" : "base_rate",
                    #     "sys": "vois",
                    #     "sum": 100,
                    #     "vat_rate": 0
                    # },
                    {
                        # "type" : "service",
                        "sys": "formax",
                        "sum": 10.25,
                        "vat_rate": 0
                    }
                ]
            }
        ]
    },
    "callback_url": "http://example.com/callback",
    "meta" : "test"
}


fm_editcontract_data = {
    "contract_id": "6298ad65-08bd-7000-0200-da9b0b14d9da",
    "agreement_type": "prolongation", # change  prolongation
    "contract_type": "14",
    "doc_date": "2022-06-02",
    "notes": "Text",
    "conditions": {
        "package": "base",
        "validity": 1,
        "validity_type": 1,
        # "service": {
        #     "sum": 99.0,
        #     "vat_rate": 20
        # },
        "rates": [
            {
                "point_id": "62617f63-5540-e000-0501-7b5fe5634e4e",
                "object_name": "coffe",
                "object_type": 1,
                "object_area": 15,
                "category_fm_id": "101",
                "address": "г. Москва, ул. Большая Якиманка, 22",
                "city": "1827",
                "usecategory_id": "5abe2e68-002c-c000-0024-883d02f16496",
                "rate_type" : 11,
                "sums": [
                    {
                        # "type" : "service",
                        "sys": "rao",
                        "sum": 100.0,
                        "vat_rate": 0,
                    },
                    {
                        # "type" : "service",
                        "sys": "vois",
                        "sum": 100.0,
                        "vat_rate": 0,
                    }
                ]
            }
        ]
    }
}

fm_editcontract_data2 = {
    "contract_id": "62bc53eb-dcb2-3000-0200-a97bd114391d",
    "agreement_type": "prolongation", # change  prolongation
    "contract_type": "15",
    "doc_date": "2022-06-29",
    "notes": "Text",
    "conditions": {
        "package": "lite",
        "validity": 31,
        "validity_type": 2,
        # "service": {
        #     "sum": 99.0,
        #     "vat_rate": 20
        # },
        "rates": [
            {
                "point_id": "625d2962-a954-3000-0501-180d5531a2cc",
                "object_name": "cyyffe",
                "object_type": 1,
                "object_area": 15,
                "category_fm_id": "101",
                "address": "г. Москва, ул. Большая Якиманка, 22",
                "city": "1827",
                "usecategory_id": "5abe2e68-002c-c000-0024-883d02f16496",
                "rate_type" : 13,  # 11 - месяц  13 - дни
                "sums": [
                    # {
                    #     "sys": "rao",
                    #     "sum": 99.0,
                    #     "vat_rate": 20
                    # },
                    # {
                    #     "sys": "vois",
                    #     "sum": 101.0,
                    #     "vat_rate": 0
                    # },
                    {
                        "type" : "base_rate",
                        "sys": "formax",
                        "sum": 31,
                        "vat_rate": 0
                    }
                ]
            }
        ]
    }
}

get_fmroles = url + '/api/external/fonmix/stuffs/contracts_access'
get_fmroles_params = {
    'p[page]' : 1,
    'p[limit]' : 1000,
    'id' : '5d1b8eca-dade-a000-0040-f2bbf9a9e89b'
    }


# Активация переподписанного договора
res_url = url + '/api/external/fonmix/contract/activate'
res_data = {
    "operation_type": 1,
    "new_contract_id": "614d9a3a-bc4f-6000-0200-fb6a2b021b0a",
    "old_contract_id": "614d97af-2140-d000-0200-6d3595f7490b ",
    "file_download_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Haanja_2010_01_1.jpg/1200px-Haanja_2010_01_1.jpg",
    "file_name": "1200px-Haanja_2010_01_1.jpg",
    "contract_formatted_data": "some data"
}



# Смена тарифа в фонмикс
fm_headers = {"Accept": "application/json, text/plain, */*",
                 "Content-Type": "application/json",
                #  "x-project-name": "crm",
                #  "x-sysowner-id": sysowner,
                 "X-Secret-Key" : "C0de69da1f5FFa7e68F05ECC6B3D9C46"
                 }


fm_change_url = "http://crm.fonmix.ru/api/red/x/task/change_packages"
fm_change_data = {
  "list": [
    {
      "external_id": "",    # ID догвоора
      "service_packages": [
        {
          "deactivate": 1,
          "external_id": "" # ID тарифа
        },
        {
          "date_end": "2022-12-31",
          "date_start": "2022-09-01",
          "external_id": "",    # ID тарифа
          "service_package_alias": "optimum"
        }
      ]
    }
  ]
}

fm_check_task_url = 'http://crm.fonmix.ru/api/red/x/task/get'
fm_check_task_data = {
    'task_id' : 16612675   # ID таски
}



fm_test = {
	"contract_type": 14,
	"region": "77",
	"doc_date": "2021-12-03",
	"category_id": "5abe2e68-002c-c000-0024-883d02f16496",
	"auto_prolongation": False,
	"executor": "10460",
	"subject": {
		"subject_type": 3,
		"country": "RUS",
		"short_name": "ИП Кагай Евгений",
		"full_name": "Индивидуальный предприниматель Кагай Евгений",
		"inn": "570502563485",
		"kpp": None,
		"ogrn": "320508100396350",
		"address": "358000, Респ Калмыкия, г Элиста",
		"employee": {
			"full_name": "Анатолий Кузьмин",
			"phone_number": "+79618083641",
			"email": "057h5dfwv9@happy-new-year.top",
			"position": "-",
			"date_beg": "2021-12-03"
		}
	},
	"conditions": {
		"package": "base",
		"date_beg": None,
		"validity": 3,
		"validity_type": 1,
		"rates": [
			{
				"object_name": "Тестовый 1",
				"object_type": 1,
				"address": "ул. Тестовая, 12",
				"usecategory_id": "5abe2e68-002c-c000-0024-883d02f16496",
				"sums": [
					{
						"type": "base_rate",
						"sys": "rao",
						"sum": 13192,
						"vat_rate": 0
					},
					{
						"type": "base_rate",
						"sys": "vois",
						"sum": 13192,
						"vat_rate": 0
					},
					{
						"type": "service",
						"sys": "formax",
						"sum": 543.68,
						"vat_rate": 0
					}
				],
				"category_fm_id": "101",
				"object_area": 500,
				"city": "1605",
				"rate_type": 11
			}
		]
	},
	"callback_url": "https:\\/\\/crm.qa.fonmix.ru\\/interface\\/red\\/secure\\/fc11d8eba651ba87a3ee46167982da55\\/task\\/activation\\/add?project=acrm&time=1638522359"
    }


fm_add_contpublic = {
    "brandObject": [],
    "brand_id": None,
    "date_beg": "2022-04-01",
    "date_end": "2022-12-31",
    "department_child_ids": ["77"],
    "department_id": "5af15183-06aa-1900-0025-ca4dd5350d32",
    "doc_date": "2022-04-01",
    "doc_number": "тестобновлениятарифов",
    "generate_doc_number": False,
    "id": None,
    "is_manual_dispatch_to_sro": True,
    "nda": 0,
    "returning": True,
    "status_code": 1,
    "subject_id": "6241d6b4-c773-3000-0100-bcc4a17e9c66",
    "sysowner_id": "00000000-0000-0000-0002-000000000003",
    "type_id": 16,
    "usecategory_id": "5abe2e68-002c-c000-0024-883d02f16496"
    }


# Авторизация Zamsha
zmauth_data = {
    "grant_type": "client_credentials",
    "client_id": "4",
    "client_secret": "MVsYksTF8Mypu7adjmiU5i5fJFBHlz2d9awXXxEM"
}

# Запрос данных от Zamsha
z_report_url = url + "/api/external/zam/receive_useobject"
z_report_data = {
"date" : "2022-05-01"
}
