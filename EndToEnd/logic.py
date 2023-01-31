#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random as rand
import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from locators import *
from selenium.webdriver.chrome.options import Options

# WINDOW_SIZE = "1920,1080"
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
# driver = webdriver.Chrome(chrome_options=chrome_options)

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(server)

assert "АСУС - Войти" in driver.title


########################################Interface#########################################

# Exception for failed test
class TestFailException(Exception):
    pass


# reload page
def reload_page():
    driver.refresh()


# quit browser
def quit_browser():
    driver.quit()


# click on object
def click(adr):
    try:
        elem = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, adr)))
        elem.click()
    except NoSuchElementException:
        raise TestFailException('Object "%s" not found' % adr)
    except TimeoutException:
        raise TestFailException('Object "%s" not found' % adr)
    else:
        return elem


# wait before clik
def waitonclick(adr):
    try:
        elem = WebDriverWait(driver, 50).until(
            ec.element_to_be_clickable((By.XPATH, adr)))
        elem.click()
    except NoSuchElementException:
        raise TestFailException('Object "%s" not found' % adr)
    except TimeoutException:
        raise TestFailException('Object "%s" not found' % adr)


# clear field
def clear(adr):
    driver.find_elements_by_xpath(adr).clear()
    return True


# write text in field
def write(adr, char):
    try:
        elem = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, adr)))
        elem.click()
        elem.clear()
        elem.send_keys(char)
    except NoSuchElementException:
        raise TestFailException('Object "%s" not found' % adr)
    except TimeoutException:
        raise TestFailException('Object "%s" not found' % adr)
    return elem


# get text of field
def get_text(adr):
    try:
        elem = driver.find_element(By.XPATH, adr)
    except NoSuchElementException:
        raise TestFailException('Object "%s" not found' % adr)
    except TimeoutException:
        raise TestFailException('Object "%s" not found' % adr)
    return elem.text


# Upload file on page
def file_upload(adr, char):
    try:
        elem = driver.find_element(By.XPATH, adr)
        elem.send_keys(char)
    except NoSuchElementException:
        raise TestFailException('Object "%s" not found' % adr)
    except TimeoutException:
        raise TestFailException('Object "%s" not found' % adr)
    return elem


# check element present on page
def checkelem(adr):
    try:
        WebDriverWait(driver, 40).until(
            ec.presence_of_element_located((By.XPATH, adr)))
    except NoSuchElementException:
        raise TestFailException('Object "%s" not found' % adr)
    except TimeoutException:
        raise TestFailException('Object "%s" not found' % adr)



# check some text on page
def checktxt(txt):
    try:
        assert txt in driver.page_source
    except AssertionError:
        raise TestFailException('Text %s not found' % txt)
    return True


# get list elements
def get_list(adr):
    try:
        # WebDriverWait(driver, 15).until(
        #     ec.presence_of_element_located((By.XPATH, adr)))
        elem = driver.find_elements_by_xpath(adr)
    except NoSuchElementException:
        raise TestFailException('Object "%s" not found' % adr)
    else:
        return elem


# check len list
def checklen(lst, ln):
    try:
        assert len(lst) == ln
    except AssertionError:
        raise TestFailException ('The list is not equal to %s' % ln)
    else:
        return True


# move cursor on element and click
def cursor_click(adr):
    try:
        elem = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, adr)))
        ActionChains(driver).move_to_element(elem).perform()
        elem.click()
    except NoSuchElementException:
        raise TestFailException('Element %s not found' % adr)


def cursor_click2(adr):
    try:
        elem = driver.find_element_by_xpath(adr)
        ActionChains(driver).move_to_element(elem).click().perform()
    except NoSuchElementException:
        raise TestFailException('Element %s not found' % adr)


###############################Classes for tests###################################


def gen_inn_fl():
    num = rand.randint(7723000001, 7723999999)
    num = str(num)
    num = [int(i) for i in num]
    a = num[0] * 7 + num[1] * 2 + num[2] * 4 + num[3] * 10 + num[4] * 3 + num[5] * 5 + num[6] * 9 + num[7] * 4 + num[8] * 6 + num[9] * 8
    n1 = int(a) % 11
    if n1 == 10:
        num.append(0)
    else:
        num.append(n1)
    b = num[0] * 3 + num[1] * 7 + num[2] * 2 + num[3] * 4 + num[4] * 10 + num[5] * 3 + num[6] * 5 + num[7] * 9 + num[8] * 4 + num[9] * 6 + num[10] * 8
    n2 = b % 11
    if n2 == 10:
        num[11] = 0
    else:
        num.append(n2)
    num = ''.join(str(i) for i in num)
    return num

def gen_inn_ul():
    num = rand.randint(662300001, 662399999)
    num = str(num)
    num = [int(i) for i in num]
    a = num[0] * 2 + num[1] * 4 + num[2] * 10 + num[3] * 3 + num[4] * 5 + num[5] * 9 + num[6] * 4 + num[7] * 6 + num[8] * 8
    n1 = int(a) % 11
    if n1 == 10:
        num.append(0)
    else:
        num.append(n1)
    num = ''.join(str(i) for i in num)
    return num


def gen_snils():
    num = rand.randint(100011001, 144999999)
    num = str(num)
    num = [int(i) for i in num]
    a = num[0] * 9 + num[1] * 8 + num[2] * 7 + num[3] * 6 + num[4] * 5 + num[5] * 4 + num[6] * 3 + num[7] * 2 + num[8] * 1
    n1 = 0
    if a < 100:
        if a >= 10:
            n1 = a
        else:
            n1 = '0' + str(a)
    elif a == 100 or a == 101:
        n1 = '00'
    else:
        n1 = a % 101
        if n1 < 10:
            n1 = '0' + str(n1)
    num.append(n1)
    num = ''.join(str(i) for i in num)
    return num


def gen_ogrn():
    num = rand.randint(100011001000, 144999999999)
    a = num % 11
    if a > 9:
        a = str(a)
        a = list(a)
        del a[0]
        a = a[0]
    else:
        a = str(a)
    num = str(num)
    ogrn = num + a
    return ogrn


def gen_ogrnip():
    num = rand.randint(30001100100001, 34499999999999)
    a = num % 13
    if a > 9:
        a = str(a)
        a = list(a)
        del a[0]
        a = a[0]
    else:
        a = str(a)
    num = str(num)
    ogrnip = num + a
    return ogrnip



def authorization(login, pas):
    elem = driver.find_element_by_name("username")
    elem.send_keys(login)
    elem = driver.find_element_by_xpath(password)
    elem.send_keys(pas)
    elem.send_keys(Keys.RETURN)
    time.sleep(3)
    return True


# Создание объекта
class Test_object():

    def __init__(self, name, owner, object_type, category, translator):
        self.name = name
        self.owner = owner
        self.object_type = object_type
        self.category = category
        self.translator = translator

    def create_object(self):
        click(objects)
        checkelem(objects_title)
        cursor_click(create_button)
        click(object_type_select)
        cursor_click(self.object_type)
        time.sleep(0.5)
        if self.object_type == object_type1:
            write(object_name, self.name)
            write(object_adres, "Москва Новый Арбат 8.75")
            write(object_index, "111111")
            write(object_owner, self.owner)
            click(object_owner1)
            write(object_desc, "Объект автотестов")
        elif self.object_type == object_type2:
            write(smi_name, self.name)
            write(smi_date_start, '01012020')
            elem = driver.find_element_by_xpath(smi_date_start)
            elem.send_keys(Keys.RETURN)
            if self.translator == 0:
                click(smi_retranslate)
            write(smi_broadcasting_time, '24')
        cursor_click(object_create)
        return True

    def add_usecategory(self):
        click(usecategory_create)
        write(select_usecategory, self.category)
        time.sleep(0.5)
        if self.category == "Предприятия общественного питания":
            click(select_usecategory1)
            time.sleep(0.5)
            write(usecategory1_field1, '50')
            write(usecategory1_field2, '100')
        if self.category == "Интернет-радио":
            click(select_usecategory2)
        click(usecategory_save)
        time.sleep(2)
        usecategory_check = f'//button[span[contains(text(), "{self.category}")]]'
        checkelem(usecategory_check)
        return True

    def search_object(self):
        click(objects)
        checkelem(objects_title)
        write(object_search, self.name)
        time.sleep(0.5)
        object_search_result = f'//td/div/a[contains(text(), {self.name})]'
        checkelem(object_search_result)
        time.sleep(1)
        cursor_click(object_search_result)
        return True

def create_object(name, subject_owner, object_type, translate):
    click(objects)
    checkelem(objects_title)
    cursor_click(create_button)
    click(object_type_select)
    cursor_click(object_type)
    time.sleep(0.5)
    if object_type == object_type1:
        write(object_name, name)
        write(object_adres, "Москва Новый Арбат 8.75")
        write(object_index, "111111")
        write(object_owner, subject_owner)
        click(object_owner1)
        write(object_desc, "Объект автотестов")
    elif object_type == object_type2:
        write(smi_name, name)
        write(smi_date_start, '01012020')
        elem = driver.find_element_by_xpath(smi_date_start)
        elem.send_keys(Keys.RETURN)
        if translate == 0:
            click(smi_retranslate)
        write(smi_broadcasting_time, '24')
    cursor_click(object_create)
    return True


# Добавление категории использования объекту
def add_object_usecategory(category_name):
    click(usecategory_create)
    write(select_usecategory, category_name)
    time.sleep(0.5)
    if category_name == "Предприятия общественного питания ( РН )":
        click(select_usecategory1)
        time.sleep(0.5)
        write(usecategory1_field1, '50')
        write(usecategory1_field2, '100')
    if category_name == "Интернет радио (ИН-Р)":
        click(select_usecategory2)
    click(usecategory_save)
    time.sleep(2)
    usecategory_check = f'//button[span[contains(text(), "{category_name}")]]'
    checkelem(usecategory_check)
    return True


# Поиск объекта
def search_object(object_name):
    click(objects)
    checkelem(objects_title)
    write(object_search, object_name)
    time.sleep(0.5)
    object_search_result = f'//td/div/a[contains(text(), {object_name})]'
    checkelem(object_search_result)
    # click(filter_button)
    # write(filter_subject, 'AU organization')
    # click(filter_subject1)
    # click(filter_accept)
    time.sleep(1)
    cursor_click(object_search_result)
    return True


# Создание субъекта
class Subject():

    def __init__(self, name, s_type, inn, kpp, ogrn, snils):
        self.name = name
        self.s_type = s_type
        self.inn = inn
        self.kpp = kpp
        self.ogrn = ogrn
        self.snils = snils


    def create_subject(self):
        click(subjects)
        checkelem(subjects_title)
        click(create_button)
        checkelem(create_menu_1)
        click(select_type)
        time.sleep(0.5)
        click(subject_type[self.s_type])
        click(select_country)
        click(country)
        if self.s_type == 'ul':
            write(ul_in_name, self.name)
            write(ul_name, "AU organization")
            write(ul_s_name, "AU ORG")
            write(ul_address, "Москва Новый Арбат")
            click(ul_address1)
            write(ul_inn, self.inn)
            if location == 'ru':
                write(ul_kpp, self.kpp)
                write(ul_ogrn, self.ogrn)
        elif self.s_type == 'fl':
            write(fl_innername, self.name)
            write(fl_firstname, 'AUfirstname')
            write(fl_secondname, 'AUsecondname')
            write(fl_thirdname, 'AUthirdname')
            write(fl_birsday, '01041990')
            write(fl_address, "Москва Новый Арбат")
            click(ul_address1)
            write(fl_passport_sery, '1608')
            write(fl_passport_number, '123456')
            write(fl_inn, self.inn)
            write(fl_snils, self.snils)
        click(subject_add)
        return True


    def add_employee(self):
        click(employees)
        click(add_employee)
        write(emloyee_fio, "Фонмикс")
        click(emloyee_position)
        cursor_click(emloyee_position1)
        write(employee_email, "test@qwe.ru")
        write(employee_phone, "89035887563")
        write(employee_date_beg, "01062020")
        click(employee_save)
        time.sleep(1)
        checkelem(emloyee_del)
        return True


    def check_filters(self):
        click(subjects)
        click(filter_button)
        waitonclick(subject_filters['typef'])
        time.sleep(0.5)
        waitonclick(subject_filters['typefs'][self.s_type])
        click(filter_accept)
        # checkelem(subject_search_result)
        return True


    def search_subject(self):
        click(subjects)
        checkelem(subjects_title)
        write(subject_search, self.name)
        time.sleep(1)
        subject_search_result = f'//div/a[contains(text(), "{self.name}")]'
        checkelem(subject_search_result)
        return True

# Поиск субъекта
def search_subject(name):
    click(subjects)
    checkelem(subjects_title)
    write(subject_search, name)
    time.sleep(1)
    subject_search_result = f'//div/a[contains(text(), "{name}")]'
    checkelem(subject_search_result)
    return True


class Contract():

    def __init__(self, number, period_b, period_e, cat):
        self.numer = number
        self.period.b = period_b
        self.period_e = period_e
        self.cat = cat

    # Создание договора
    def create_contract(subject_name, category):
        if 'Договоры' not in driver.title:
            click(contracts)
            time.sleep(1)
        checkelem(contracts_title)
        click(create_button)
        click(contract_type)
        waitonclick(contract_type1)
        write(contract_subject, subject_name)
        time.sleep(1)
        click(contract_subject1)
        write(contract_center, 'Москва')
        time.sleep(0.5)
        waitonclick(contract_center1)
        write(doc_date, '01012021')
        write(date_beg, '01082021')
        write(date_end, '31082022')
        write(contract_cat, category)
        contract_cat1 = f'//ul/li[span[contains(text(), "{category}")]]'
        waitonclick(contract_cat1)
        click(contract_region_button)
        cursor_click(contract_region)
        time.sleep(0.5)
        click(contract_create)
        return True



# Создание договора
def create_contract(subject_name, category):
    if 'Договоры' not in driver.title:
        click(contracts)
        time.sleep(1)
    checkelem(contracts_title)
    click(create_button)
    click(contract_type)
    waitonclick(contract_type1)
    write(contract_subject, subject_name)
    time.sleep(1)
    click(contract_subject1)
    write(contract_center, 'Москва')
    time.sleep(0.5)
    waitonclick(contract_center1)
    write(doc_date, '01012021')
    write(date_beg, '01082021')
    write(date_end, '31082022')
    write(contract_cat, category)
    contract_cat1 = f'//ul/li[span[contains(text(), "{category}")]]'
    waitonclick(contract_cat1)
    click(contract_region_button)
    cursor_click(contract_region)
    time.sleep(0.5)
    click(contract_create)
    return True


# Создание договора 2й вариант
def add_contract(profile, category, dat_start, dat_end):   #профиль договора, категория, дата начала, дата окончания
    if "АСУС - Договоры" not in driver.title:
        click(contracts)
    waitonclick(create_button)
    waitonclick(contract_type)
    if profile == 'VOIS':
        waitonclick(contract_type1)
    elif profile == 'RAO':
        waitonclick(contract_type1)
    elif profile == 'FORMAX':
        waitonclick(contract_type3)
    write(contract_subject, 'ООО')
    waitonclick(contract_subject1)
    write(contract_center, 'Москва')
    waitonclick(contract_center1)
    write(doc_date, dat_start)
    write(date_beg, dat_start)
    write(date_end, dat_end)
    write(contract_cat, category)
    contract_cat1 = f'//ul/li[span[contains(text(), "{category}")]]'
    waitonclick(contract_cat1)
    if profile == 'FORMAX':
        waitonclick(contract_region_button)
        waitonclick(contract_region)
    waitonclick(contract_create)
    return True


# Поиск договора
def search_contrat(number):
    if "АСУС - Договоры" not in driver.title:
        click(contracts)
    checkelem(contracts_title)
    time.sleep(2)
    click(filter_reset)
    write(contract_search, number)
    time.sleep(2)
    contract_search_result = f'//div/a[contains(text(), "{number}")]'
    checkelem(contract_search_result)
    # click(filter_button)
    # write(filter_subject, 'AU organization')
    # time.sleep(0.5)
    # waitonclick(filter_subject1)
    # click(filter_accept)
    # time.sleep(1)
    # checkelem(contract_search_result)
    click(contract_search_result)
    time.sleep(2)
    checkelem(title_info)
    return True


# Добавление условия оплаты
def add_common_condition(dat):
    waitonclick(terms)
    checkelem(title_terms)
    cursor_click(add_term)
    click(term_common)
    click(pay_period)
    time.sleep(0.5)
    cursor_click(pay_period1['month'])
    write(pay_date, '1')
    click(peni)
    waitonclick(peni_var['fix'])
    write(peni_rate, '50')
    click(report_period)
    time.sleep(0.5)
    cursor_click(report_period1['month'])
    write(report_time, '1')
    click(fine)
    time.sleep(3)
    click(fine_var['fix'])
    write(fine_rate, '50')
    click(fonmix_select)
    time.sleep(0.5)
    cursor_click(fonmix_off)
    # write(common_date, dat)
    click(common_save)
    time.sleep(1)
    return True


# Добавление ставки по объекту фикс
def add_object_rate_fix(object_name):
    click(terms)
    waitonclick(add_term)
    waitonclick(term_rate)
    click(rate_variant)
    time.sleep(0.5)
    waitonclick(rate_variants['object_fix'])
    write(select_object_rate, object_name)
    time.sleep(1)
    cursor_click(select_object_rate1)
    click(object_rate_usecategory)
    time.sleep(0.5)
    cursor_click(object_rate_usecategory1)
    click(main_rate)
    write(start_period, '01082021')
    write(rate_sum, '100')
    click(rate_save)
    time.sleep(1)
    checkelem(rate_check)
    return True



# Добавление ставки по объекту фикс с сезонными ставками
def add_object_rate_fix_season(object_name):
    click(terms)
    waitonclick(add_term)
    waitonclick(term_rate)
    click(rate_variant)
    time.sleep(0.5)
    waitonclick(rate_variants['object_fix'])
    write(select_object_rate, object_name)
    time.sleep(1)
    cursor_click(select_object_rate1)
    click(object_rate_usecategory)
    time.sleep(0.5)
    cursor_click(object_rate_usecategory1)
    click(main_rate)
    write(start_period, '01012021')
    write(rate_sum, '1000')
    click(season_rate)
    write(start_season_period, '0106')
    write(end_season_period, '3006')
    write(season_sum, '2000')
    click(rate_save)
    time.sleep(1)
    checkelem(rate_check)
    return True


# Добавление ставки по объекту FORMAX
def add_object_rate_formax(val, perc, name_obj, service, start_date, pay, sea_beg, sea_end, sea_pay, cou_day):    # сколько объектов добавить, тип ставки, имя объекта, в скольки объектах будет услуга, начало периода, сумма, сезон начало, сезон окончание, сезон сумма, сколько действует дневная ставка
    if 'АСУС - Условия' not in driver.title:
        waitonclick(terms)
    dxx = 0
    exx = service
    for i in range(val):
        waitonclick(add_term)
        waitonclick(term_rate)
        click(rate_variant)
        time.sleep(0.5)
        if perc != 'fix' and perc != 'day':
            waitonclick(rate_variants['object_%'])
        elif perc == 'fix':
            waitonclick(rate_variants['object_fix'])
        elif perc == 'day':
            waitonclick(rate_variants['object_day'])

        write(select_object_rate, name_obj)
        time.sleep(2)
        obj = get_list(select_object_rate1)
        obj[dxx].click()
        click(object_rate_usecategory)
        time.sleep(0.5)
        waitonclick(object_rate_usecategory_universal)

        if start_date != 'n' and pay != 'n':                    # добавлять ли основную ставку
            if perc != 'day':
                waitonclick(main_rate)
                write(start_period, start_date)
                click(object_change_profile_button)
                waitonclick(object_change_profile_rao)

                if perc == 'fix':
                    write(rate_sum, pay)
                    waitonclick(main_rate)
                    start2 = get_list(start_period)
                    sum2 = get_list(rate_sum)
                    time.sleep(1)
                    start2[1].send_keys(start_date)
                    sum2[1].send_keys(pay)

                elif perc != 'fix' and perc != 'day':
                    write(rate_percent, perc)
                    write(min_sum, pay)
                    waitonclick(main_rate)
                    start2 = get_list(start_period)
                    sum2 = get_list(min_sum)
                    perc2 = get_list(rate_percent)
                    time.sleep(1)
                    start2[1].send_keys(start_date)
                    sum2[1].send_keys(pay)
                    perc2[1].send_keys(perc)

            elif perc == 'day':
                write(start_day_period, start_date)
                write(count_days, cou_day)
                write(sum_rate_day, pay)

        if exx > 0 and perc == 'fix':                          #  Условия услуги
            waitonclick(service_rate_button)
            write(service_rate_start, start_date)
            write(service_rate_sum, pay)
        elif exx > 0 and perc != 'fix' and perc != 'day':
            waitonclick(service_rate_button)
            write(service_rate_start, start_date)
            write(service_rate_perc, perc)
            write(service_min_sum, pay)

        if sea_beg != 'n' and sea_end != 'n' and sea_pay != 'n':    # условие сезонной ставки
            waitonclick(season_rate)
            write(start_season_period, sea_beg)
            write(end_season_period, sea_end)
            waitonclick(change_profile_season_button)
            waitonclick(change_profile_season_rao)

            if perc == 'day' or perc == 'fix':
                write(season_sum, sea_pay)
                waitonclick(season_rate)
                st_seas = get_list(start_season_period)
                end_seas = get_list(end_season_period)
                sum_seas = get_list(season_sum)
                time.sleep(1)
                st_seas[1].send_keys(sea_beg)
                end_seas[1].send_keys(sea_end)
                sum_seas[1].send_keys(sea_pay)

            elif perc != 'day' and perc != 'fix':
                write(perc_season, perc)
                write(min_sum_season, sea_pay)
                waitonclick(season_rate)
                time.sleep(1)
                st_seas = get_list(start_season_period)
                end_seas = get_list(end_season_period)
                per_seas = get_list(perc_season)
                sum_seas = get_list(min_sum_season)
                time.sleep(1)
                st_seas[1].send_keys(sea_beg)
                end_seas[1].send_keys(sea_end)
                per_seas[1].send_keys(perc)
                sum_seas[1].send_keys(sea_pay)

        click(rate_save)
        time.sleep(2)
        checklen(get_list(rate_check), (1 + dxx))
        dxx += 1
        exx -= 1
    return True


# Добавление ставки по объекту
def add_obj_rate(val, perc, start_date, val_obj, pay, sea_beg, sea_end, sea_pay):      # сколько объектов добавить, % ставки, начало периода, название объектов, сумма, сезон начало, сезон окончание, сезон сумма
    if 'АСУС - Условия' not in driver.title:
        waitonclick(terms)
    list_count = 0
    for i in range(val):
        waitonclick(add_term)
        waitonclick(term_rate)
        waitonclick(rate_variant)
        checkelem(rate_variants['object_%'])

        val_list = len(get_list(rate_check))

        if perc != 'fix':
            waitonclick(rate_variants['object_%'])
        elif perc == 'fix':
            waitonclick(rate_variants['object_fix'])

        checkelem(select_object_rate)
        write(select_object_rate, val_obj)
        checkelem(select_object_rate1)
        list_dinamic = get_list(select_object_rate1)
        list_dinamic[list_count].click()
        list_count += 1
        waitonclick(object_rate_usecategory)
        waitonclick(object_rate_usecategory_universal)

        if start_date != 'n' and pay != 'n':
            click(main_rate)
            if perc == 'fix':
                write(start_period, start_date)
                write(rate_sum, pay)
            elif perc != 'fix':
                write(start_period, start_date)
                write(rate_percent, perc)
                write(min_sum, pay)

        if sea_beg != 'n' and sea_end != 'n' and sea_pay != 'n':
            click(season_rate)
            write(start_season_period, sea_beg)
            write(end_season_period, sea_end)
            write(season_sum, sea_pay)

        waitonclick(rate_save)
        time.sleep(2)
        checklen(get_list(rate_check), (val_list + 1))
    return True


# добавление коэффициентов
def add_koefficets(coef, val, start, end):       #  тип коэффициента, значение коэффициента, начало действия, конец действия если нужно
    if 'АСУС - Условия' not in driver.title:
        waitonclick(terms)

    stim = len(get_list(coef_elem_stimul))
    netw = len(get_list(coef_elem_network))
    stim_for = len(get_list(coef_elem_formax))
    waitonclick(add_term)
    waitonclick(term_coef)
    waitonclick(coef_name_button)
    if coef == 'network':
        checkelem(coef_network)
        waitonclick(coef_network)
    elif coef == 'stimul':
        checkelem(coef_stimul)
        waitonclick(coef_stimul)
    elif coef == 'formax':
        checkelem(coef_stimul_formax)
        waitonclick(coef_stimul_formax)

    write(coef_start, start)
    if end != 'n':
        write(coef_end, end)

    waitonclick(coef_values_button)
    checkelem(coef_values)
    time.sleep(1)
    list_coef = get_list(coef_values)
    list_coef[val].click()
    waitonclick(coef_save_button)

    if coef == 'network':
        checkelem(coef_elem_network)
        checklen(get_list(coef_elem_network), (netw + 1))
    elif coef == 'stimul':
        checkelem(coef_elem_stimul)
        checklen(get_list(coef_elem_stimul), (stim + 1))
    elif coef == 'formax':
        checkelem(coef_elem_formax)
        checklen(get_list(coef_elem_formax), (stim_for + 1))
    return True


# закрыть начисления
def close_accurals(val):        # сколько начислений нужно закрыть
    if 'АСУС - Начисления' not in driver.title:
        click(accruals)
        time.sleep(3)

    el_re = len(get_list(elems_reward))

    click(add_accurals_button)
    click(close_accurals_button)
    checkelem(checkbox_close)
    list_accruals = get_list(checkbox_close)

    if val == 'all':
        for vex in range(len(list_accruals)):
            click(checkbox_close)
    else:
        for vex in range(val):
            click(checkbox_close)

    click(accept_close)
    click(close_form)

    if val == 'all':
        reload_page()
        time.sleep(2)
        waitonclick(add_accurals_button)
        time.sleep(2)
        checklen(get_list(elems_reward), 0)
    else:
        reload_page()
        checkelem(elems_reward)
        time.sleep(1)
        checklen(get_list(elems_reward), (el_re - val))
    return True


 # Добавление ставки по договору
def add_contract_rate(perc, start_date, suma):             # выбор типа ставки, дата начала, сумма ставки
    if 'АСУС - Условия' not in driver.title:
        waitonclick(terms)

    waitonclick(add_term)
    waitonclick(term_rate)
    waitonclick(rate_variant)
    checkelem(rate_variants['contract_fix'])

    if perc == 'fix':
        waitonclick(rate_variants['contract_fix'])
        waitonclick(c_main_rate)
        write(c_start_period, start_date)
        write(c_rate_sum, suma)

    elif perc != 'fix':
        waitonclick(rate_variants['contract_%'])
        waitonclick(c_main_rate)
        write(c_start_period, start_date)
        write(c_rate_percent, perc)
        write(c_min_sum, suma)

    waitonclick(rate_save)
    checkelem(rate_check)
    checklen(get_list(rate_check), 1)
    return True


# Добавлеие услуги
def add_service(arg, beg, stop, pay):           # разовое или нет, дата начала, дата окончания если надо, оплата
    if 'АСУС - Условия' not in driver.title:
        waitonclick(terms)
    waitonclick(add_term)
    waitonclick(term_service)

    if arg == 'one_off':
        waitonclick(service_one_off_checkbox)

    if stop != 'n':
        write(service_date_end, f'{stop}')

    write(service_date_beg, f'{beg}')
    write(service_sum, f'{pay}')
    waitonclick(service_save)
    time.sleep(1)
    return True


#Генерация начислений на выбранный период
def generic_accurals_on_period(val, err):        # на какой период генерировать начисления, должно быть сообщение об ошибке
    if 'АСУС - Начисления' not in driver.title:
        time.sleep(3)
        click(accruals)
        time.sleep(1)
        reload_page()
        time.sleep(3)

    waitonclick(add_accurals_button)
    waitonclick(generic_on_period_button)
    waitonclick(list_generic_on_period)

    if val == 'three':
        waitonclick(choose_three_month)
    elif val == 'six':
        waitonclick(choose_six_month)
    elif val == 'nine':
        waitonclick(choose_nine_month)
    elif val == 'twelve':
        waitonclick(choose_twelve_month)

    waitonclick(start_generic_on_period)

    if err != 'n':
        checkelem(report_err_not_equal)
        assert get_text(report_err_not_equal) == 'Формирование начислений на выбранный период невозможно. Автопролонгация отключена'
        waitonclick(cancel_generic_button)
    elif err == 'n':
        time.sleep(2)
        waitonclick(add_accurals_button)
    return True


def add_percent_rate_object(object_name):
    click(terms)
    waitonclick(add_term)
    waitonclick(term_rate)
    click(rate_variant)
    time.sleep(0.5)
    waitonclick(rate_variants['object_%'])
    write(select_object_rate, object_name)
    time.sleep(1)
    cursor_click(select_object_rate1)
    click(object_rate_usecategory)
    time.sleep(0.5)
    cursor_click(object_rate_usecategory2)
    write(pice_of_AB, '0')
    click(main_rate)
    write(start_period, '01012021')
    write(rate_percent, '10')
    write(min_sum, '100')
    click(rate_save)
    time.sleep(1)
    checkelem(rate_check)
    return True


# перевод договора в статус действует
def activate_contract(number):
    checkelem(cont_status['project'])
    click(cont_status_button['on_sugest'])
    checkelem(cont_status['sugest'])
    click(cont_status_button['on_sign'])
    time.sleep(0.5)
    write(contract_number, number)
    write(contract_director, 'Автодиретор')
    write(contract_director_p, '+79097896523')
    write(contract_director_e, 'qwe@qwe.com')
    write(contract_booker, 'Автобухгалтер')
    write(contract_booker_p, '+79097896523')
    write(contract_booker_e, 'qwe@qwe.com')
    write(contract_employe, 'Автосодрудник')
    write(contract_employe_p, '+79097896533')
    write(contract_employe_e, 'ewq@qwe.com')
    click(edit_accept)
    time.sleep(1)
    # click(edit_accept)
    # time.sleep(1)
    checkelem(cont_status['sign'])
    click(cont_status_button['in_active'])
    waitonclick(activate_yes)
    time.sleep(1)
    checkelem(cont_status['active'])
    return True


# перевод договора в статус действует 2й вариант
def activate_contract2():
    checkelem(cont_status['project'])
    click(cont_status_button['on_sugest'])
    write(contract_director, 'Автодиретор')
    write(contract_director_p, '+79097896523')
    write(contract_director_e, 'qwe@qwe.com')
    write(contract_booker, 'Автобухгалтер')
    write(contract_booker_p, '+79097896523')
    write(contract_booker_e, 'qwe@qwe.com')
    write(contract_employe, 'Автосодрудник')
    write(contract_employe_p, '+79097896533')
    write(contract_employe_e, 'ewq@qwe.com')
    click(edit_accept)
    time.sleep(1)
    checkelem(cont_status['sugest'])
    click(cont_status_button['on_sign'])
    waitonclick(generate_cont_number)
    click(edit_accept)
    time.sleep(1)
    checkelem(cont_status['sign'])
    click(cont_status_button['in_active'])
    click(edit_accept)
    time.sleep(1)
    checkelem(cont_status['active'])
    return True


# Перевод договора в статус "Согласование расторжения"
def agree_on_termination():
    checkelem(cont_status['active'])
    click(cont_status_button['on_agree_termination'])
    click(reason_for_termination_button)
    waitonclick(reason_for_termination)
    write(termination_date, '01022021')
    write(docu_date, '01012021')
    click(sign_indebt_button)
    waitonclick(sign_indebt_at_work)
    write(comment_field, 'Autotest')
    file_upload(termination_add_file, testfile)
    click(sign_report_button)
    waitonclick(sign_report_no)
    write(period_no_report, '1')
    click(termination_accept_button)
    checkelem(cont_status['agree_termination'])
    click(button_files_in_contract)
    time.sleep(1)
    checklen(get_list(contract_count_files), 1)
    return True


# Перевод договора в статус "Расторжение"
def on_termination():
    checkelem(cont_status['agree_termination'])
    click(cont_status_button['on_agree_termination'])
    file_upload(termination_add_file, testfile2)
    click(termination_accept_button)
    checkelem(cont_status['termination'])
    checklen(get_list(contract_count_files), 2)
    return True


# Перевод договора в статус "Согласование закрытия"
def agree_on_close():
    checkelem(cont_status['termination'])
    click(cont_status_button['on_agree_termination'])
    click(sign_indebt_button)
    waitonclick(sign_indebt_no_prospects)
    click(sign_report_button)
    waitonclick(sign_report_yes)
    waitonclick(close_accept_button)
    checkelem(cont_status['agree_closed'])
    return True


# Перевод договора в статус "Закрыт"
def on_close():
    checkelem(cont_status['agree_closed'])
    click(cont_status_button['on_close'])
    waitonclick(edit_accept)
    checkelem(cont_status['closed'])
    return True


# Идентификация платежа
def ident_payment(cont_number, payment):
    click(payments)
    time.sleep(1)
    assert "АСУС - Платежи" in driver.title
    write(search_payment, payment)
    identification = f'//td/div/span[@id="payment_ident-{payment}"]'
    click(identification)
    write(search_ident_payment, cont_number)
    time.sleep(0.5)
    ident_on_contract_button = f"//button[@data-id = 'ident-on-contract-{cont_number}']"
    cursor_click(ident_on_contract_button)
    cursor_click(ident_yes)
    time.sleep(0.5)
    remove_ident = f"//button[@data-id = 'rm-ident-on-contract-{cont_number}']"
    checkelem(remove_ident)
    action = ActionChains(driver)
    action.send_keys(Keys.ESCAPE)
    action.perform()
    return True


# идентификация платежа 2й вариант
def ident_payment_new(payment):
    con = get_text(contract_name)
    click(payments)
    time.sleep(1)
    assert "АСУС - Платежи" in driver.title
    write(search_payment, payment)
    identification = f'//td/div/span[@id="payment_ident-{payment}"]'
    click(identification)
    write(search_ident_payment, con)
    time.sleep(0.5)
    ident_on_contract_button = f"//button[@data-id = 'ident-on-contract-{con}']"
    cursor_click(ident_on_contract_button)
    cursor_click(ident_yes)
    time.sleep(0.5)
    remove_ident = f"//button[@data-id = 'rm-ident-on-contract-{con}']"
    checkelem(remove_ident)
    action = ActionChains(driver)
    action.send_keys(Keys.ESCAPE)
    action.perform()
    click(contracts)
    time.sleep(1)
    search_contrat(con)
    return True


# сопоставить начисление
def compare_accurals(cont_number, payment):
    click(cont_comparsion)
    time.sleep(0.5)
    check_ident_payment = f"//tr/td/div[contains(text(), '{payment}')]"
    checkelem(check_ident_payment)
    click(compare_arrow)
    click(compare_period)
    click(compare_yes_button)
    time.sleep(0.5)
    click(compare_arrow)
    checkelem(compare_balance)
    return True


# Создание отчета
def add_report(contract, tobject, report_type):
    click(reports)
    time.sleep(1)
    assert "АСУС - Список отчетов" in driver.title
    click(report_add)
    time.sleep(1)
    report_contract1 = f'//ul/li[contains(text(), "{contract}")]'
    write(report_contract, contract)
    time.sleep(1)
    waitonclick(report_contract1)
    write(report_period_start, '01082021')
    write(report_period_end, '31082021')
    write(report_date, '01092021')
    click(report_type_select)
    if report_type == 'mp':
        waitonclick(report_mp)
    if report_type == 'trk':
        waitonclick(report_trk)
        write(val_cash, '1000')
        write(percent_AB, '10')
    write(report_summ, '100')
    report_objects = f'//div[contains(text(), "{tobject}")]'
    click(report_objects)
    time.sleep(0.3)
    click(report_object_add)
    file_upload(report_file, testfile)
    click(report_save)
    click(report_save_1)
    checkelem(report_number_check)
    return True


# создать начисление по отчёту, Мелкая публичка
def create_accural_report(typ, beg, end, perc, val_sum, rep_sum):     # тип отчёта, дата начала, дата окончания, % если нужно, сумма ВАЛ, сумма отчёта
    con = get_text(contract_name)
    click(reports)
    time.sleep(2)
    assert "АСУС - Список отчетов" in driver.title
    waitonclick(report_add)
    checkelem(report_contract)
    write(report_contract, con)
    time.sleep(1)
    report_contract1 = f'//ul/li[contains(text(), "{con}")]'
    waitonclick(report_contract1)
    write(report_period_start, beg)
    write(report_period_end, end)
    write(report_date, beg)
    click(report_type_select)

    if typ == 'mp%' or typ == 'mp':
        waitonclick(report_mp)
    elif typ == 'trk':
        waitonclick(report_trk)

    if typ != 'mp':
        write(val_cash, val_sum)

    if perc != 'n':
        write(percent_AB, perc)

    if typ == 'mp%' or typ == 'trk' or typ == 'mp':
        write(report_summ, 999)

    click(check_box_all_access_obj)
    waitonclick(transfer_to_choice)
    time.sleep(0.5)
    waitonclick(report_object_add)
    file_upload(report_file, testfile)

    if typ == 'mp%' or typ == 'trk' or typ == 'mp':
        click(report_save)
        click(report_save_1)

    if typ == 'mp%' or typ == 'trk':
        checkelem(report_error_more_less1)
        err_txt = get_text(report_error_more_less1)
        assert err_txt ==  'Разница между суммой отчёта и расчётной суммой не должна превышать 1', 'Иная ошибка или отсутствует'

    if typ != 'mp%' and typ != 'trk':
        checkelem(report_err_not_equal)
        err_txt = get_text(report_err_not_equal)
        assert err_txt == 'Сумма отчета не соответствует сумме начислений не подтвержденных отчетами для выбранных объектов', 'Иная ошибка или отсутствует'

    write(report_summ, rep_sum)
    click(report_save)
    click(report_save_1)
    checkelem(report_number_check)
    click(contracts)
    time.sleep(1)
    search_contrat(con)
    return True


# удалить отчёты
def del_report(val):        # сколько отчётов удалить
    if 'АСУС - Отчеты' not in driver.title:
        waitonclick(button_report_in_contract)
        checkelem(button_del_report_in_contract)
        time.sleep(1)
    for i in range(val):
        val_re = len(get_list(button_del_report_in_contract))
        waitonclick(button_del_report_in_contract)
        reload_page()
        time.sleep(2)
        checklen(get_list(button_del_report_in_contract), (val_re - 1))
    return True



# создать доп соглашение
def create_additional_agree(start_date):
    click(button_subord_doc)
    waitonclick(add_subord_button)
    click(subord_doc_type_button)
    waitonclick(subord_doc_type)
    click(generic_subord_number)
    write(subord_start_date, start_date)
    write(subord_doc_date, start_date)
    waitonclick(accept_create_subord_doc)
    time.sleep(1)
    return True


# исключение объекта
def exeption_rate(ty_rate, val, numb, season, only):  # тип ставки, название объекта, какой объект из списка, сезонная ставка, только сезонная ставка или все
    if 'АСУС - Условия' not in driver.title:
        waitonclick(terms)
    waitonclick(add_term)
    waitonclick(term_rate)
    waitonclick(rate_variant)
    time.sleep(1)

    if ty_rate == 'obj_fix':
        waitonclick(rate_variants['object_fix'])
        time.sleep(2)
        click(search_by_button)
        waitonclick(search_by)
    elif ty_rate == 'obj_perc':
        waitonclick(rate_variants['object_%'])
        time.sleep(2)
        click(search_by_button)
        waitonclick(search_by)

    write(select_object_rate, val)
    checkelem(select_object_rate1)
    time.sleep(1)
    obj_count = get_list(select_object_rate1)
    obj_count[numb].click()
    waitonclick(object_rate_usecategory)
    waitonclick(object_rate_usecategory_universal_subord)

    if only == 'all' or only == 'main':
        waitonclick(object_exeption_button)
        checkelem(button_exeption_check)

    if season == 'yes' and only != 'all':
        click(exeption_season_button)
        checkelem(button_exeption_check)
    waitonclick(rate_save)
    time.sleep(2)
    return True


# перевод  доп соглашения в статус действует
def activate_additional_doc():
    checkelem(cont_status['project'])
    click(cont_status_button['on_sugest'])
    click(edit_accept)
    checkelem(cont_status['sugest'])
    waitonclick(cont_status_button['on_sign'])
    click(edit_accept)
    checkelem(cont_status['sign'])
    waitonclick(cont_status_button['in_active'])
    click(edit_accept)
    checkelem(cont_status['active'])
    time.sleep(1)
    waitonclick(return_to_main)
    time.sleep(2)
    return True


# проверка работы фильтрации во вкладке Условия
def check_cond_filter_work(typ, descr, reas, reas_count, reas_val):   # тип, описание, основание, какое основание, кол-во условий после применённого основания
    if 'АСУС - Условия' not in driver.title:
        waitonclick(terms)
        time.sleep(2)

    con = get_text(contract_name)

    reload_page()
    time.sleep(2)
    cas = len(get_list(cond_all_statuses))
    checklen(get_list(cond_status_applied), cas)

    if reas != '1' or reas == 'all':
        click(cond_filter_type_button)
        time.sleep(2)
        waitonclick(filter_type_var[typ])
        time.sleep(2)
        all_typ = len(get_list(cond_all_types))
        checklen(get_list(elems_type_cond[typ]), all_typ)

        if typ == 'rate':
            click(cond_filter_desciption_button)
            time.sleep(2)
            waitonclick(filter_description_var[descr])
            time.sleep(2)

            if descr == 'delete':
                assert 'Удаление' in get_text(choose_descr), 'удаление отсутствует'
            elif descr == 'add':
                assert 'Добавление' in get_text(choose_descr), 'добавление отсутствует'
            elif descr == 'change':
                assert 'Изменение' in get_text(choose_descr), 'изменение отсутствует'

    if reas == '1' or reas == 'all':

        write(cond_filter_reason_button, (con+'/ДС'))
        checkelem(choose_reas)
        time.sleep(3)
        exx = get_list(choose_reas)
        time.sleep(2)
        exx[reas_count].click()
        time.sleep(2)
        checklen(get_list(cond_all_types), reas_val)
    return True


# проверка на присутствие начислений, их количества
def check_accurals_type(type_acc, count_val):     # тип начисления, сколько должно быть
    if 'АСУС - Начисления' not in driver.title:
        waitonclick(accruals)
        time.sleep(3)

    waitonclick(add_accurals_button)

    if type_acc == 'rew':
        checklen(get_list(elems_reward), count_val)
    elif type_acc == 'rew_obj':
        checklen(get_list(elems_reward_object), count_val)
    elif type_acc == 'rew_cont':
        checklen(get_list(elems_reward_contract), count_val)
    elif type_acc == 'rew_repo':
        checklen(get_list(elems_reward_report), count_val)
    elif type_acc == 'service':
        checklen(get_list(elems_service), count_val)
    return True


# проверка значений начисления
def check_accurals_values(suma, val_sum):       # сумма начисления, количество одинаковых сумм
    if 'АСУС - Начисления' not in driver.title:
        waitonclick(accruals)
        checkelem(elems_reward)
        time.sleep(2)
    sum_a = f'//td[5]/div[contains(text(),  "{suma}")]'
    checklen(get_list(sum_a), val_sum)
    return True


# проверка типов в сопоставлении
def check_acc_in_compars_type(type_acc, count_val):      # тип начисления, сколько должно быть
    if 'АСУС - Сопоставление' not in driver.title:
        waitonclick(cont_comparsion)
    time.sleep(2)
    reload_page()
    time.sleep(2)
    waitonclick(compare_arrow_open)
    time.sleep(2)
    if type_acc == 'rew':
        checklen(get_list(elems_reward), count_val)
    elif type_acc == 'rew_obj':
        checklen(get_list(elems_reward_object), count_val)
    elif type_acc == 'rew_cont':
        checklen(get_list(elems_reward_contract), count_val)
    elif type_acc == 'rew_repo':
        checklen(get_list(elems_reward_report), count_val)
    reload_page()
    time.sleep(2)
    return True


# проверка значений в сопоставлениях
def check_acc_in_compars_values(suma, val_sum):       # сумма начисления, количество одинаковых сумм
    if 'АСУС - Сопоставление' not in driver.title:
        waitonclick(cont_comparsion)
    time.sleep(2)
    reload_page()
    time.sleep(2)
    waitonclick(compare_arrow_open)
    time.sleep(2)
    sum_a = f'//td[5]/div/b[contains(text(),  "{suma}")]'
    checklen(get_list(sum_a), val_sum)
    reload_page()
    time.sleep(2)
    return True


# проверка связей отчётов с начислениями
def check_accural_report_connect(suma, val_sum, val_dis):    # сумма отчёта, количество сумм, количество заблокированных кнопок
    if 'АСУС - Начисления' not in driver.title:
        waitonclick(accruals)
        time.sleep(2)
        waitonclick(add_accurals_button)
    sum_a = f'//td[7]/div[contains(text(),  "{suma}")]'
    checklen(get_list(sum_a), val_sum)
    checklen(get_list(create_report_button_dis), val_dis)
    checklen(get_list(write_off_button_dis), val_dis)
    return True


# добавление и проверка разовых начислений
def add_one_of_accurals(one_type, pay):      # выбор типа начисления
    if 'АСУС - Начисления' not in driver.title:
        time.sleep(4)
        click(accruals)
        time.sleep(1)
        reload_page()
        time.sleep(4)

    waitonclick(add_accurals_button)
    click(add_one_off_button)
    waitonclick(button_accural_type)
    time.sleep(3)
    waitonclick(accural_type[one_type])

    if one_type in ('fine', 'penalty', 'debit_debt'):
        click(one_off_recovery_view)
        waitonclick(one_off_recovery_view_var)
        click(one_off_sysowner)
        waitonclick(one_off_var_sysowner)
        click(one_off_nds)
        waitonclick(one_off_nds_var)

    elif one_type in  ('comp_pre_judical', 'comp_judical', 'accomp_music'):
        click(one_off_sysowner)
        waitonclick(one_off_var_sysowner)
        click(one_off_nds)
        waitonclick(one_off_nds_var)

    elif one_type == 'big_license':
        write(one_off_date_end, '31122021')
        write(one_off_date_beg, '01012021')

    write(one_off_date_beg, '01012021')
    write(one_off_sum_field, pay)
    click(create_one_off_button)
    reload_page()
    time.sleep(3)

    if one_type == 'fine':
        checklen(get_list(elems_fine), 1)
    elif one_type == 'penalty':
        checklen(get_list(elems_penalty), 1)
    elif one_type == 'debit_debt':
        checklen(get_list(elems_debit_debt), 1)
    elif one_type == 'pre_judical':
        checklen(get_list(elems_pre_judical), 1)
    elif one_type == 'judical':
        checklen(get_list(elems_judical), 1)
    elif one_type == 'accomp_music':
        checklen(get_list(elems_accomp_music), 1)
    elif one_type == 'big_license':
        checklen(get_list(elems_big_license), 1)
    return True


# проверка на присутствие всех разовых начислений во вкладке "Сопоставления"
def check_one_off_in_comparsion(typ, val):    # тип начисления, количество
    if 'АСУС - Сопоставление' not in driver.title:
        waitonclick(cont_comparsion)
    waitonclick(compare_arrow_open)
    time.sleep(2)
    if typ == 'all':
        checklen(get_list(elems_judical), val)
        checklen(get_list(elems_pre_judical), val)
        checklen(get_list(elems_fine), val)
        checklen(get_list(elems_penalty), val)
        checklen(get_list(elems_debit_debt), val)
        checklen(get_list(elems_accomp_music), val)
        checklen(get_list(elems_big_license), val)
    elif typ == 'judical':
        checklen(get_list(elems_judical), val)
    elif typ == 'pre_judical':
        checklen(get_list(elems_pre_judical), val)
    elif typ == 'fine':
        checklen(get_list(elems_fine), val)
    elif typ == 'penalty':
        checklen(get_list(elems_penalty), val)
    elif typ == 'debit_debt':
        checklen(get_list(elems_debit_debt), val)
    elif typ == 'accomp_music':
        checklen(get_list(elems_accomp_music), val)
    elif typ == 'big_license':
        checklen(get_list(elems_big_license), val)
    reload_page()
    return True


#проверка на присутствие всех разовых начислений во вкладке "Начисления"
def check_all_one_off_in_accural():
    if 'АСУС - Начисления' not in driver.title:
        time.sleep(2)
        click(accruals)
        checkelem(elems_fine)
    checklen(get_list(elems_fine), 1)
    checklen(get_list(elems_penalty), 1)
    checklen(get_list(elems_debit_debt), 1)
    checklen(get_list(elems_pre_judical), 1)
    checklen(get_list(elems_judical), 1)
    checklen(get_list(elems_accomp_music), 1)
    checklen(get_list(elems_big_license), 1)
    return True


# списание начисления, без комментов и добавленных файлов
def write_off_accurals(val, reason, summ):          # какое по счёту начисление списать, причина списания, сумма списания
    if 'АСУС - Начисления' not in driver.title:
        time.sleep(3)
        click(accruals)
        time.sleep(1)
        reload_page()
        checkelem(write_off_button)
        time.sleep(2)

    di = get_list(write_off_button)
    di[val].click()
    waitonclick(write_off_reason_button)
    if reason == 'debit_debt':
        waitonclick(write_off_reason_debit_debt)
    elif reason == 'pause':
        waitonclick(write_off_reason_pause)
    write(write_off_sum, summ)
    waitonclick(write_off_save)

    if reason == 'debit_debt':
        write(one_off_date_beg, '01012021')
        click(one_off_sysowner)
        waitonclick(one_off_var_sysowner)
        click(one_off_nds)
        waitonclick(one_off_nds_var)
        click(one_off_recovery_view)
        waitonclick(one_off_recovery_view_var)
        click(create_one_off_button)
    reload_page()
    time.sleep(3)
    return True


# выбрать профиль
def choose_profile(prof):
    waitonclick(profile_button)
    time.sleep(1)
    if prof == 'VOIS':
        waitonclick(profile_vois)
    elif prof == 'RAO':
        waitonclick(profile_rao)
    elif prof == 'FORMAX':
        waitonclick(profile_formax)
    time.sleep(4)
    return True


# расширенная информация о начислении по объекту
def accural_arrow_info():
    list_all_accural = (get_list(elems_reward_object))
    list_all_accural[0].click()
    return True


# проверка работы переключателя "Сгруппировать по периоду"
def check_switcher_period():
    rxx = len(get_list(elems_reward))
    click(switcher_button)
    time.sleep(6)
    dxx = len(get_list(elems_reward_object_vois))
    exx = len(get_list(elems_reward_object_rao))
    assert ((exx + dxx) == (rxx * 2)), 'Не разгруппировано'
    return True
