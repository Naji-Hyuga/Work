#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#from sys import argv
import os
import requests
import json
import time
import api_tests as t
import crm_api as c
# import main

# a, x = argv
x = "fm_check_task"


headers = t.authcrm(c.auth_url, c.fmauth_data, c.auth_headers)
# headers = t.authcrm(c.auth_url, c.fmauth_data, c.fm_headers)

if x == "change_tarif":

    subject = c.chekSubject_data
    subject["ogrn"] = c.ogrn
    t.fonmix_check(subject, headers)


if x == "create14":
    fm_addcontract_data = c.fm_addcontract_data
    c.exist = {"id" : c.subjects['ru']}
    fm_addcontract_data["subject"] = c.exist
    fm_addContract = t.requestPost(c.fm_addcontract, fm_addcontract_data, headers)
    # print(fm_addContract.text)
    print(json.loads(fm_addContract.text))


if x == "create14n":
    fm_addcontract_data = c.fm_addcontract_data
    fm_addcontract_data["subject"] = c.new
    fm_addContract = t.requestPost(c.fm_addcontract, fm_addcontract_data, headers)
    print(json.loads(fm_addContract.text))

if x == "create15":
    fm_addcontract_data = c.fm_addcontract_data2
    c.exist = {"id" : c.subjects['ru']}
    fm_addcontract_data["subject"] = c.exist
    fm_addContract = t.requestPost(c.fm_addcontract, fm_addcontract_data, headers)
    print(json.loads(fm_addContract.text))

if x == "edit14":
    # fm_editcontract_data = c.fm_editcontract_data
    # fm_editcontract_data["subject"] = c.exist
    fm_editcontract_data = c.fm_editcontract_data
    fm_editContract = t.requestPost(c.fm_editcontract, fm_editcontract_data, headers)
    print(json.loads(fm_editContract.text))

if x == "edit15":
    fm_editcontract_data = c.fm_editcontract_data2
    fm_editContract = t.requestPost(c.fm_editcontract, fm_editcontract_data, headers)
    print(json.loads(fm_editContract.text))

if x == 'check_role':
    fm_contract_roles = t.requestGet(c.get_fmroles, c.get_fmroles_params, headers)
    print(json.loads(fm_contract_roles.text))


if x == "change_tarif":
    contract_id = '603cbc05-2e32-7000-0200-8b116a5d38e3'
    old_tarif = '60f558a3-6670-d000-0000-61b951dbb4f3'
    new_tarif = '603d0497-039b-f000-0000-c78d4516c516'
    date_start = '2021-03-01'
    date_end = '2022-12-31'
    tariff_name = 'simple'
    fm_change_data = c.fm_change_data
    fm_change_data["list"][0]["external_id"] = contract_id
    fm_change_data["list"][0]["service_packages"][0]["external_id"] = old_tarif
    fm_change_data["list"][0]["service_packages"][1]["external_id"] = new_tarif
    fm_change_data["list"][0]["service_packages"][1]["date_start"] = date_start
    fm_change_data["list"][0]["service_packages"][1]["date_end"] = date_end
    fm_change_data["list"][0]["service_packages"][1]["service_package_alias"] = tariff_name
    fm_change_tarif = t.requestPost(c.fm_change_url, fm_change_data, c.fm_headers)
    print(json.loads(fm_change_tarif.text))

if x == 'fm_check_task':
    task_id = '18154224'
    c.fm_check_task_data['task_id'] = task_id
    fm_check_task = t.requestGet(c.fm_check_task_url, c.fm_check_task_data, c.fm_headers)
    print(json.loads(fm_check_task.text))


if x == "zam_report":
    headers = t.authcrm(c.auth_url, c.zmauth_data, c.auth_headers)
    zam_report = t.requestPost(c.z_report_url, c.z_report_data, headers)
    print(json.loads(zam_report.text))

if x == 'test':
    fm_addcontract_data = c.fm_test
    c.exist = {"id" : c.subjects['ru']}
    fm_addcontract_data["subject"] = c.exist
    fm_addContract = t.requestPost(c.fm_addcontract, fm_addcontract_data, headers)
    print(json.loads(fm_addContract.text))
