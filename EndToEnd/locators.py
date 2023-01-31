#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
import os


test = "https://crm-test.k8s.id-network.ru"
preprod = "https://crm-preprod.k8s.id-network.ru"
hottfix = "https://crm-hotfix.k8s.id-network.ru"
kgz = "https://crm-kgz-hotfix.dev.k8s.id-network.ru"
dev = 'https://crm-dev.k8s.id-network.ru/'
server = test
if os.getenv('preprod'):
    server = preprod
if os.getenv('hotfix'):
    server = hottfix
if os.getenv('kgz'):
    server = kgz

location = 'ru'
if server == kgz:
    location = 'kgz'

unic = datetime.strftime(datetime.now(), "%m%d%H%M%S") # Уникальная переменная
testname = 'test' + unic
testpayment = '00005331'
if server == preprod:
    testpayment = '02093077' # preprod
if server == hottfix:
    testpayment = '01865446'
testobject = 'AUtestobject'+unic
testsubject = "AUtestsubject"+unic
cont_number = 'AU'+unic
contract_name = "//div[1]/div[3]//a[2]"
testfile = os.path.abspath("Autotests/TestFiles/test.txt")
testfile2 = os.path.abspath("Autotests/TestFiles/test2.py")
# period =

password = "//input[@type='password']"

# Main menu
contracts = '//a[@href="/vois/contracts"]'
reports =   '//a[@href="/vois/reports"]'
payments =  '//a[@href="/vois/finance"]'
comparsion = '//a[@href="/vois/comparison"]'
userdev = '//a[@href="/vois/userdevelopment"]'
events = '//a[@href="/vois/events"]'
comits = '//a[@href="/vois/commits"]'
statements = '//a[@href="/vois/statements"]'
analytics = '//a[@href="/vois/analytics"]'
statcontracts = '//a[@href="/vois/statistic/contracts"]'
statcontnoreport = '//a[@href="/vois/statistic/contracts-without-reports"]'
subjects = '//a[@href="/vois/subjects"]'
objects = '//a[@href="/vois/objects"]'


profile_button = "//div[3]/div[2]/div[2]/span"
profile_vois = "//li[contains(text(), 'ВОИС')]"
profile_rao = "//li[contains(text(), 'РАО')]"
profile_formax = "//li[contains(text(), 'ФОРМАКС')]"


filter_button = '//div/button/span[contains(text(), "Фильтр")]'
filter_accept = '//div/button[span[contains(text(), "Применить")]]'
filter_reset = '//button[@id = "0244v19vn"]'


# Object filters
object_search = '//div/input[@placeholder="Поиск"]'
filter_subject = '//div/input[@placeholder="Субъект"]'
filter_subject1 = '//ul/li/span/strong'
type_object = '//div/input[@placeholder="Тип объекта"]'
filter_web = '//div/input[@placeholder="Сеть"]'
filter_address = '//div/input[@placeholder="Введите адрес"]'


# Subject filters
subject_search = '//div/input[@placeholder="Поиск по имени и коду"]'
subject_filters = {
    'typef' : '//div/input[@placeholder="Тип"]',
    'typefs' : {'fl' : '//div/ul/li[span[contains(text(), "Физическое лицо")]]',
                'ul' : '//div/ul/li[span[contains(text(), "Юридическое лицо")]]'},
    'status' : '//div/input[@placeholder="Статус"]',
    'statuses' : {'active' : '//div/ul/li[span[contains(text(), "Действует")]]',
                  'no_active' : '//div/ul/li[span[contains(text(), "Не действует")]]'},
    'inn' : '//div/input[@placeholder="ИНН"]',
    'kpp' : '//div/input[@placeholder="КПП"]',
    'ogrn' : '//div/input[@placeholder="ОГРН"]',
    'snils' : '//div/input[@placeholder="СНИЛС"]'
    }


# Contract filters
contract_search = '//div/input[@id="fm7o1rgoi"]'


create_button = '//button/span[contains(text(), "Создать")]'


# Create subjects
subjects_title = '//div[contains(text(), "Субъекты")]'
create_menu_1 = '//div[@class="el-dialog__wrapper subject-create"]'
select_type = '//div[@class="el-col el-col-8"][1]'
subject_type = {'ul' : '//ul/li/span[contains(text(), "Юридическое")]',
                'fl' : '//ul/li/span[contains(text(), "Физическое")]'}
select_country = '//div[@class="el-col el-col-8"][2]'
country = '//ul/li/span[contains(text(), "RUS - Россия")]'
ul_in_name = '//div[label[contains(text(), "Внутреннее наименование")]]/div/div/input'
ul_name = '//div[label[contains(text(), "Наименование")]]/div/div/input'
ul_s_name = '//div[label[contains(text(), "Сокр. наименование")]]/div/div/input'
ul_address = '//div/input[@placeholder="Выберите адрес"]'
ul_address1 = '//div/ul/li[@title = "г Москва, ул Новый Арбат"]'
ul_inn = '//div/input[@placeholder="ИНН"]'
ul_kpp = '//div/input[@placeholder="КПП"]'
ul_ogrn = '//div/input[@placeholder="ОГРН"]'
fl_innername = '//input[1][@id="2kksg3ykq"]'
fl_firstname = '//input[2][@id="2kksg3ykq"]'
fl_secondname = '//input[@id="2kksg3ykq"][3]'
fl_thirdname = '//input[@id="2kksg3ykq"][4]'
fl_birsday = '//input[@id="v97a3199k"]'
fl_address = '//input[@id="zh62sz6os"]'
fl_passport_sery = '//input[@id="fro2i1syk"][1]'
fl_passport_number = '//input[@id="fro2i1syk"][2]'
fl_inn = '//input[@id="fro2i1syk"][3]'
fl_snils = '//input[@id="qjl48uzup"]'
subject_add = '//div/div/button[span[contains(text(), "Добавить")]]'
subject_cancel = '//div/div/button[span[contains(text(), "Отмена")]]'


#Subject card
employees = '//a[contains(text(), "Сотрудники")]'
add_employee = '//button[@id="bjs5sslj3"]'
emloyee_fio = '//input[@id="ima2ko65h"]'
emloyee_position = '//input[@id="pb56duvhe"]'
emloyee_position1 = '//ul/li/span[contains(text(), "Сотрудник")]'
employee_email = '//input[@id="8uv3w8nvx"]'
employee_phone = '//input[@id="jrsdgzes3"]'
employee_date_beg = '//input[@id="glf2tuiwl"]'
employee_save = '//button[@id="em6uakeky"]'
emloyee_del = '//button[@id="exi6m3ktp"]'


# Create object
oo = '//div[@class="el-dialog__wrapper object__dialog"]'
objects_title = '//div[contains(text(), "Объекты")]'
object_type_select = '//div[label[contains(text(), "Тип объекта")]]/div/div/div/input'
object_type1 = '//li/span[contains(text(), "Физический объект")]'
object_type2 = '//li/span[contains(text(), "СМИ")]'
object_name = '//div[contains(text(), "Наименование")]/div/input'
object_adres = '//div/input[@id="zh62sz6os"]'
object_index = '//div[label[contains(text(), "Почтовый индекс")]]/div/div/input'
object_web = '//div[contains(text(), "Сеть")]/div/div/input'
object_web1 = '//div/div/div/ul/li[span[contains(text(), "Автотесты")]]'
object_owner = '//div[contains(text(), "Субъект")]/div/div/input'
object_owner1 = '//ul/li/span/strong'
object_desc = '//div[label[contains(text(), "Примечание")]]/div/div/textarea'
object_cancel = '//button[span[contains(text(), "Отмена")]]'
object_create = '//button[@id="y868s8mvb"]'
smi_name = '//input[@id="3cgsxy1y2"]'
smi_date_start = '//input[@id="ebkqet0e4"]'
smi_retranslate = '//label[@id="ltrrdv6uz"]'
smi_broadcasting_time = '//input[@id="lic_volume"]'


# object card
usecategory_create = '//button[@id = "mtnxv0qd6"]'
select_usecategory = '//input[@id = "hj881o93j"]'
select_usecategory1 = '//ul/li[span[contains(text(), "Предприятия общественного питания ( РН )")]]'
select_usecategory2 = '//ul/li[span[contains(text(), "Интернет-радио ( ИН-Р )")]]'
usecategory1_field1 = '//input[@id = "tz3umgzib_5"]'
usecategory1_field2 = '//input[@id = "tz3umgzib_9"]'
usecategory_save = '//button[@id = "z0sq1r1jq"]'


# create contract
contracts_title = '//div[contains(text(), "Договоры")]'
contract_type = '//input[@id = "58zhcobj5"]'
contract_type1 = '//ul/li[span[contains(text(), "Договор с пользователем (ВОИС)")]]'
contract_type2 = '//span[contains(text(), "Договор с пользователем (РАО)")]'
contract_type3 = '//span[contains(text(), "Договор с пользователем (Формакс)")]'
contract_subject = '//input[@id = "ctt5gi24f"]'
contract_subject1 = '//ul/li/span/strong'
contract_number = '//input[@id = "hmvdm1fv2"]'
contract_center = '//input[@id = "wg5ho7hqa"]'
contract_center1 = '//ul/li[span[contains(text(), "Москва и МО")]]'
contract_region_button = '//input[@id="2t5qz2tbk"]'
contract_region = '//div/ul/li[span[contains(text(), "Москва г")]]'
doc_date = '//input[@id = "45yszqi4d"]'
date_beg = '//input[@id = "5icmyu1ps"]'
date_end = '//input[@id = "2eno3qkrm"]'
contract_cat = '//input[@id = "8w2xqiuqb"]'
contract_cat1 = '//ul/li[span[contains(text(), "Предприятия общественного питания ( РН )")]]'
contract_cat2 = '//ul/li[span[contains(text(), "Интернет-радио ( ИН-Р )")]]'
contract_web = '//input[@id = "yu6h7mdyw"]'
contract_web1 = '//ul/li[span[contains(text(), "Автотесты")]]'
contract_director = '//input[@id="ndf4553v1"]'
contract_director_p = '//input[@id="ndi845v1"]'
contract_director_e = '//input[@id="n545vd3v1"]'
contract_booker = '//input[@id="nd34553v1"]'
contract_booker_p = '//input[@id="nd3845v1"]'
contract_booker_e = '//input[@id="n535vd3v1"]'
contract_employe = '//input[@id="ndf4453v1"]'
contract_employe_p = '//input[@id="ndi445v1"]'
contract_employe_e = '//input[@id="n5454d3v1"]'
contract_create = '//button[@id = "epmvf7gld"]'


# contract card
title_info = '//div[contains(text(), "Информация")]'
title_terms = '//div[contains(text(), "Условия")]'
cont_status = {
    'project' : '//tr[td/span[contains(text(), "Статус")]]/td[contains(text(), "Проект")]',
    'sugest' : '//tr[td/span[contains(text(), "Статус")]]/td[contains(text(), "Согласование проекта")]',
    'sign' : '//tr[td/span[contains(text(), "Статус")]]/td[contains(text(), "Согласован")]',
    'active' : '//tr[td/span[contains(text(), "Статус")]]/td[contains(text(), "Действует")]',
    'rework' : '//tr[td/span[contains(text(), "Статус")]]/td[contains(text(), "Доработка")]',
    'no_contract_use' : '//tr[td/span[contains(text(), "Статус")]]/td[contains(text(), "Бездоговорное использование")]',
    'bin' : '//tr[td/span[contains(text(), "Статус")]]/td[contains(text(), "Корзина")]',
    'agree_termination' : '//tr[td/span[contains(text(), "Статус")]]/td[contains(text(), "Согласование расторжения")]',
    'termination' : '//tr[td/span[contains(text(), "Статус")]]/td[contains(text(), "Расторжение")]',
    'agree_closed' : '//tr[td/span[contains(text(), "Статус")]]/td[contains(text(), "Согласование закрытия")]',
    'closed' : '//tr[td/span[contains(text(), "Статус")]]/td[contains(text(), "Закрыт")]'
}
cont_status_button = {
    'on_sugest' : '//button[@id = "to_status_3"]',
    'on_sign' : '//button[@id = "to_status_4"]',
    'in_active' : '//button[@id = "to_status_10"]',
    'on_rework' : '//button[@id = "to_status_2"]',
    'no_contract_use' : '//button[@id = "to_status_9"]',
    'in_bin' : '//button[@id = "to_status_100"]',
    'on_agree_termination' : '//button[@id="3pom6vfv7"]',
    'on_close' : '//button[@id="5aea94b6-0312-4400-0020-838dfca3ff00"]'

}
activate_yes = '//button[span[contains(text(), "Да")]]'

edit_button = '//button[@id = "0koqs6nr0"]'
edit_accept = '//button[@id = "rs31d8wyt"]'
accruals = '//a[contains(text(), "Начисления")]'
generate_cont_number = '//button[@id="4rh7ynxc6"]'


# condition tab
terms = '//a[contains(text(), "Условия")]'
add_term = '//button[@id = "bkk64bobf"]'
term_common = '//button[@id = "common"]'
term_rate = '//button[@id = "rate"]'
term_coef = '//button[@id = "coefficient"]'
term_service = '//button[@id = "service"]'
term_event = '//button[@id = "event"]'
cond_filter_type_button = "//input[@id='mx0vu756a']"
cond_all_types = "//tbody/tr/td[2]"
cond_filter_desciption_button = "//input[@id='r2pht2wka']"
cond_filter_reason_button = "//input[@id='ew3f8fvs1']"
cond_status_applied = "//div[contains(text(), 'Применено')]/span"
cond_all_statuses = '//tr/td[1]/div'
elem_service = "//div[contains(text(), 'Услуги с фиксированой ставкой')]"

choose_descr = '//td[3]'
choose_reas = '//div[@x-placement="bottom-start"]//li/span'

elems_type_cond = {
    'rate' : "//td/div[contains(text(), 'Ставка')]"
}

filter_type_var = {
    'pay_rep' : "//li/span[contains(text(), 'Порядок оплат и отчетности')]",
    'coef' : "//li/span[contains(text(), 'Коэффициент')]",
    'event' : "//li/span[contains(text(), 'Мероприятие')]",
    'serv_fix' : "//li/span[contains(text(), 'Услучи с фиксированой ставкой')]",
    'rate' : "//li/span[contains(text(), 'Ставка')]",
    'adv_pay' : "//li/span[contains(text(), 'Авансовый платёж')]",
    'change_param' : "//li/span[contains(text(), 'Изменение основных параметров договора')]",
    'obj_rate' : "//li/span[contains(text(), 'Ставки по объектам')]",
    'tarif' : "//li/span[contains(text(), 'Тариф')]"

}

filter_description_var = {
    'add' : "//li/span[contains(text(), 'Добавление')]",
    'change' : "//li/span[contains(text(), 'Изменение')]",
    'delete' : "//li/span[contains(text(), 'Удаление')]"

}


# condition service form
service_sum = '//input[@id="et1xkfw4t"]'
service_date_beg = '//input[@id="q65qgatcp"]'
service_date_end = '//input[@id="8clezuhrq"]'
service_save = '//button[@id="qciapy47c"]'
service_one_off_checkbox = '//span[@class="el-checkbox__inner"]'


# contract on termination form
reason_for_termination_button = ('//input[@id="i23sydnj8"]')
reason_for_termination = '//ul/li/span[contains(text(), "Соглашение о расторжении")]'
sign_report_button = '//input[@id="ofgywcf545"]'
sign_report_no = '//span[contains(text(), "Не предоставлена")]'
sign_report_yes = '//span[contains(text(), "Предоставлена")]'
period_no_report = '//input[@type="number"]'
sign_indebt_button = '//input[@id="1ou5cp5vq"]'
sign_indebt_at_work = '//ul/li/span[contains(text(), "В работе по взысканию")]'
sign_indebt_no_prospects = '//ul/li/span[contains(text(), "Нет перспектив")]'
termination_date = "//input[@id='g1w76idz9']"
docu_date = "//input[@id='ds2ku58r4']"
comment_field = "//textarea[@id='ofgywcf5o']"
termination_add_file = '//input[@name="file"]'
termination_accept_button = '//button[@id="pjqmuf7nl"]'
close_accept_button = '//button[@id="cagn72795"]'


#coefficient form
coef_name_button = '//input[@id="ti04is7ak"]'
coef_network = '//span[contains(text(), "Сетевой коэффициент")]'
coef_stimul = '//span[contains(text(), "Стимулирующий коэффициент")]'
coef_stimul_formax = '//span[contains(text(), "Стимулирующий коэффициент Формакс")]'
coef_values_button = '//input[@id="w744xo9g4"]'
coef_values = '//div[@x-placement="bottom-start"]//li/span'
coef_start = '//input[@id="v05g3bmqx"]'
coef_end = '//input[@id="o9robti7b"]'
coef_save_button = '//button[@id="65ofph698"]'
coef_elem_stimul = "//div[contains(text(), 'Стимулирующий коэффициент')]"
coef_elem_network = "//div[contains(text(), 'Сетевой коэффициент')]"
coef_elem_formax = "//div[contains(text(), 'Стимулирующий коэффициент Формакс')]"


# files in card contract
contract_count_files = '//button/i[@class="el-icon-delete"]'
button_files_in_contract = '//a[contains(text(), "Файлы")]'


# report tab
button_report_in_contract = '//a[contains(text(), "Отчеты")]'
button_del_report_in_contract = '//button[@id="kp67qdpi3"]'


# accurals
ac_reward_nd = '//tr[@class="el-table__row"]'    # нет задолженности
ac_reward_d = '//tr[@class="el-table__row paid-row"]'       # задолженность
elems_reward = '//div[contains(text(), "Вознаграждение")]'
elems_reward_object = '//div[contains(text(), "Вознаграждение - Объект")]'
elems_reward_object_vois = '//div[contains(text(), "Вознаграждение - Объект (ВОИС)")]'
elems_reward_object_rao = '//div[contains(text(), "Вознаграждение - Объект (РАО)")]'
elems_reward_contract = '//div[contains(text(), "Вознаграждение - Договор")]'
elems_reward_report = "//div[contains(text(), 'Вознаграждение - По отчету')]"
elems_judical = '//div[contains(text(), "Компенсация по суду")]'
elems_pre_judical = '//div[contains(text(), "Компенсация досудебная")]'
elems_fine = '//div[contains(text(), "Штраф")]'
elems_penalty = "//div[contains(text(), 'Пени')]"
elems_debit_debt = "//div[contains(text(), 'Дебиторская задолженность')]"
elems_accomp_music = "//div[contains(text(), 'Сопроводительная музыка к БП')]"
elems_big_license = "//div[contains(text(), 'Большие права')]"
elems_service = "//div[contains(text(), 'Услуги')]"

close_accurals_button = '//button[@id="j0jalq5gk"]'
close_accurals_button_disabled = '//button[@id="j0jalq5gk"][@disabled="disabled"]'
empty_accurals = '//div[@class="el-table__empty-block"]'
add_accurals_button = '//button[@id="p57190bc2"]'
generic_on_period_button = '//button[@id="zaf47u1ha"]'
list_generic_on_period = "//input[@id='natjzuvgs']"
choose_three_month = '//span[contains(text(), "3 месяца")]'
choose_six_month = '//span[contains(text(), "6 месяцев")]'
choose_nine_month = '//span[contains(text(), "9 месяцев")]'
choose_twelve_month = '//span[contains(text(), "12 месяцев")]'
cancel_generic_button = '//button[@id="90eua9kud"]'
start_generic_on_period = "//button[@id='eggqjutp6']"
add_one_off_button = '//button[@id="85h4ux3oo"]'

values_into_accural = "//td/div/a[@target='_blank']"
arrow_accurals = '//div/i[@class="el-icon el-icon-arrow-right"]'
switcher_button = '//span[@class="el-switch__core"]'

all_accural = "//tr/td[11]/div"

create_report_button_dis = "//button[@disabled='disabled'][@id='1su0bwcg9']"
write_off_button_dis = "//button[@disabled='disabled'][@id='99kwux4vu']"


# form one off accurals
create_one_off_button = "//button[@id='2x5czf2ph']"
button_accural_type = "//input[@id='jbpfhetpt']"
all_of_accural_type = "//div[4]//li"
accural_type = {
    'fine' : "//span[contains(text(), 'Штраф')]",
    'penalty' : "//span[contains(text(), 'Пени')]",
    'debit_debt' : "//span[contains(text(), 'Дебиторская задолженность')]",
    'comp_pre_judical' : "//span[contains(text(), 'Компенсация досудебная')]",
    'comp_judical' : "//span[contains(text(), 'Компенсация по суду')]",
    'accomp_music' : "//span[contains(text(), 'Сопроводительная музыка к БП')]",
    'big_license' : "//span[contains(text(), 'Большие права')]"
}

one_off_sum_field = "//input[@id='pdypopqhm']"
one_off_date_beg = "//input[@id='0mvsakc70']"
one_off_date_end = "//input[@id='cs5qxmpsc']"
one_off_sysowner = "//input[@id='ujnzamupi']"
one_off_var_sysowner = "//li/span[contains(text(), 'ВОИС')]"
one_off_nds = "//input[@id='eu76myj2d']"
one_off_nds_var = "//li/span[contains(text(), 'Без НДС')]"
one_off_recovery_view = "//input[@id='97u7qycpp']"
one_off_recovery_view_var = "//li/span[contains(text(), 'Досудебное начисление')]"


# form write off accurals
write_off_button = "//button[@id='99kwux4vu']"
write_off_reason_button = "//input[@id='4kdcnavsd']"
write_off_reason_debit_debt = "//span[contains(text(), 'Дебиторская задолженность')]"
write_off_reason_pause = "//span[contains(text(), 'Расторжение/Приостановление')]"
write_off_sum = "//input[@id='rgnmuolke']"
write_off_save = '//button[@id="e93yoqfdf"]'


# close accurals form
checkbox_close = '//label[@id="dj8ad4ixo"][@class="el-checkbox"]'
accept_close = '//button[@id="yygtrlstr"]'
close_form = '//div[2]//div[4]//button/i'  # переделать локатор


# common term
pay_period = '//input[@id = "5o8d8bx13"]'
pay_period1 = {'month' : '//ul/li[@id = "5o8d8bx13-1" ]'}
pay_date = '//input[@id = "9vhqbopcy"]'
peni = '//input[@id = "t4hfiwqtf"]'
peni_var = {'fix' :'//li[@id = "t4hfiwqtf-1"]',
            'proc' : '//li[@id = "t4hfiwqtf-2"]'
 }
peni_rate = '//input[@id = "1bat1gbzn"]'
report_period = '//input[@id = "esijk48nd"]'
report_period1 = {'month' : '//ul/li[@id = "esijk48nd-1"]'}
fine = '//input[@id = "vvlohchuv"]'
fine_var = {'fix' :'//li[@id = "vvlohchuv-1"][span[contains(text(), "Фикс. сумма")]]',
            'proc' : '//li[@id = "vvlohchuv-2"]'
 }
fine_rate = '//input[@id = "nvc0wh1cv"]'
report_time = '//input[@id = "q115719e0"]'
fonmix_select = '//input[@id = "h3hohlod2"]'
fonmix_on = '//li[@id="vvlohchuv-0"][span[contains(text(), "Да")]]'
fonmix_off = '//li[@id="vvlohchuv-1"][span[contains(text(), "Нет")]]'
report_form = '//input[@id = "kf5bbgas2"]'
report_form1 = {'paper' : '//ul/li[span[contains(text(), "На бумажном носителе")]]'}
report_address = '//input[@id = "bq2mlx5uh"]'
common_date = '//input[@id = "q21inq68t"]'
common_save = '//button[@id = "3sj25x18h"]'


# rate object\contract
rate_variant = '//input[@id = "oro914q3i"]'
rate_variants = {
    'object_fix' : '//ul/li[span[contains(text(), "По объекту - фикс.сумма")]]',
    'object_%' : '//ul/li[span[contains(text(), "По объекту - %")]]',
    'object_day' : "//span[contains(text(), 'По объекту - фикс сумма по дням')]",
    'contract_fix' : '//ul/li[span[contains(text(), "По договору - фикс.сумма")]]',
    'contract_%' : '//ul/li[span[contains(text(), "По договору - %")]]'
                }

# contract fix
c_main_rate = '//button[@id="gw4mdpjwn"]/span'
c_start_period = '//input[@id="77vqj6ydq"]'
c_rate_sum = '//input[@id = "8tkhfs8oo"]'


# contract percent
c_rate_percent = '//input[@id = "t08nt0iop"]'
c_min_sum = '//input[@id = "r6nqhhvxx"]'


# object fix
select_object_rate = '//input[@id = "6x58b07jm"]'
select_object_rate1 = '//ul/li/b'
object_rate_usecategory = '//input[@id = "h8wb4rrlh"]'
object_rate_usecategory1 = '//ul/li[span[contains(text(), "Предприятия общественного питания")]]'
object_rate_usecategory2 = '//ul/li[span[contains(text(), "Интернет-радио")]]'
object_rate_usecategory_universal = '//div[6]//li/span'
object_rate_usecategory_universal_subord = "//div[7]//li/span"
main_rate = '//button[@id = "1e1ceocxp"]'
start_period = '//input[@id = "8jrryzbpz"]'
rate_sum = '//input[@id = "9tvvmc8rn"]'
rate_save = '//button[@id = "sn7mafc29"]'
rate_check = '//tr/td/div[contains(text(), "Ставка")]'
object_exeption_button = "//button[@id='1eo8lcfi7']"
button_exeption_check = "//button/span[contains(text(), 'Исключена')]"
exeption_season_button = "//button[@id='sjbxw1cqi']"
object_change_profile_button = '//input[@id="gs35qp0ug"]'
object_change_profile_rao = "//span[contains(text(), 'РАО')]"


#object season
season_sum = '//input[@id = "3rrxdfma1"]'
season_rate = '//button[@id = "8avm689nz"]'
start_season_period = '//input[@id = "ytf7zvuxr"]'
end_season_period = '//input[@id = "2jz2qmgpc"]'
perc_season = '//input[@id="mn0s2htrc"]'
min_sum_season = '//input[@id="8o3sbkh6k"]'
change_profile_season_button = '//input[@id="3dbibq5gm"]'
change_profile_season_rao = '//div[@x-placement="bottom-start"]//span[contains(text(), "РАО")]'

#object service
service_rate_button = '//button[@id="1e1ceocxp6"]'
service_rate_start = '//input[@id="8jrryzbpz6"]'
service_rate_sum = '//input[@id="9tvvmc8rn6"]'
service_rate_perc = '//input[@id="k9kvq82wf6"]'
service_min_sum = '//input[@id="heudlipmg6"]'


#object day
start_day_period = '//input[@id = "8j365bpz6"]'
count_days = '//input[@id="k9k4421f45"]'
sum_rate_day = '//input[@id="k9k122145"]'


# object fix by subord
search_by_button = "//input[@id='yi7iab22x']"
search_by = '//span[contains(text(), "Включенным объектам")]'


# object percent
pice_of_AB = '//input[@id="5z4o1v53z"]'
rate_percent = '//input[@id="k9kvq82wf"]'
min_sum = '//input[@id="heudlipmg"]'


# cont_comparsion
cont_comparsion = '//a[contains(text(), "Сопоставление")]'
check_ident_payment = f"//tr/td/div[contains(text(), {testpayment})]"
compare_arrow = f'//tr[@class = "el-table__row payment-qa-id-{testpayment}"]'
compare_period = "//tr[2]//tr[td/div[contains(text(), 'МС.08.2021')]]/td/div/button[@id = '80rzrdivd']"
compare_yes_button = '//button[@id="vg8fsp79x"]'
compare_balance = "//tr[td/div[contains(text(), 'МС.08.2021')]]/td/div/b[contains(text(), '0,00')]"
compare_arrow_open = '//i[@class="el-icon el-icon-arrow-right"]'


# contract accurals
accrual_summ = "//td[@class='el-table_1_column_5 is-center']/div"


# Payments
search_payment = '//input[@id="vb671uij2"]'
identification = f'//td/div/span[@id="payment_ident-{testpayment}"]'
search_ident_payment = '//input[@id="kd7hqqezr"]'
ident_on_contract_button = f"//button[@data-id = 'ident-on-contract-{cont_number}']"
remove_ident = f"//button[@data-id = 'rm-ident-on-contract-{cont_number}']"
ident_yes = '//button[@class="el-button el-button--default el-button--small el-button--primary ident-qa-confirm"]'
ident_close = '//button[@aria-label="Close"]'


# reports
report_add = '//button[@id="zgpuhl5h5"]'
report_search = '//input[@id="ool7rw1di"]'



# report form
report_contract = '//input[@id="9c8vllvjl"]'
report_contract1 = f'//ul/li[contains(text(), {cont_number})]'
report_period_start = '//input[@id="0e5dkke43"]'
report_period_end = '//input[@id="nhtc9njlw"]'
report_date = '//input[@id="hqk4z01g6"]'
report_summ = '//input[@id="wrsbt9bnx"]'
report_type_select = '//input[@id="zcbvtszfy"]'
check_box_all_access_obj = "//div[1]/p/label/span[1]/span"
transfer_to_choice = "//button[@class='el-button el-button--primary el-button--medium el-transfer__button']"
report_error_more_less1 = '//span[@class="error-message__item"]'
report_err_not_equal = '//b[@class="error-message__title"]'


# report types
report_mp = '//ul/li/span[contains(text(), "Мелкая публичка")]'
report_mpe = '//ul/li/span[contains(text(), "Мероприятие (мелкая публичка)")]'
report_tech = '//ul/li/span[contains(text(), "Технический отчёт")]'
report_trk = '//ul/li/span[contains(text(), "ТРК")]'
report_event = '//ul/li/span[contains(text(), "Мероприятие")]'
val_cash = '//input[@id="48g8c5mts"]'
percent_AB = '//input[@id="a68izccnm"]'
total_sum = '//input[@id="5rlo8k6dm"]'
report_objects = f'//div[contains(text(), {testobject})]'
report_object_add = '//button/span/i[@class="el-icon-arrow-right"]'
report_file = '//div/input[@id="report_file_upload"]'
report_save = '//button[@id="6pa33ha6o"]'
report_save_1 = '//ul/li[@id="report_status_1"]'
report_number_check = '//div/label[contains(text(), "Номер отчета")]'
report_number_field = '//div[label[contains(text(), "Номер отчета")]]/div'


# subord documents
button_subord_doc = '//a[contains(text(), "Подчиненные документы")]'
add_subord_button = "//button[@id='o0evhg166']"
return_to_main = "//div/span/a"


# subord documents, create form
subord_doc_type_button = "//input[@id='58zhcobj5']"
subord_doc_type = '//span[contains(text(), "Дополнительное соглашение")]'
generic_subord_number = '//button[@id="dd27yd3hk"]'
subord_doc_date = "//input[@id='jiwv4wxoz']"
subord_start_date = "//input[@id='crp2g1k3t']"
accept_create_subord_doc = '//button[@id="epmvf7gld"]'
