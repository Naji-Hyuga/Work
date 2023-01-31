#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import logic as f
import locators as l
import test_suites as t


passed_test_count = 0
failed_test_count = 0


f.authorization("crmuser@test.api", "user123")


def rus():
    test_suite = [

        t.subject.create_subject(),
        t.subject.add_employee(),

        t.phis_object.create_object(),
        t.phis_object.add_usecategory(),

            t.smi_object.create_object(),
        # t.smi_object.add_usecategory(),

        # t.retsmi_object.create_object(),
        # t.retsmi_object.add_usecategory(),

        # t.translate_smi_contract(),
        t.fixrate()
    ]
    return test_suite


def kgz():
    test_suite = [
    t.subject.create_subject(),
    t.phis_object_kgz.create_object(),
    t.phis_object_kgz.add_usecategory(),
    t.fixrate
    ]
    return test_suite


def test():
    test_suite = [
        f.search_contrat("AU0128143454"),
        f.close_all_accurals()
    ]
    return test_suite


def test2():
    test_suite = [
        f.create_contract('Нарсис Дрен', 'Предприятия общественного питания')
    ]
    return test_suite


run = rus()



for i in run:
    if i is True:
        passed_test_count +=1
    else:
        failed_test_count += 1
print ('Test finished with %s PASSED and %s FAILED' % (passed_test_count, failed_test_count))
