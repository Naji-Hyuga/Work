
# Настройка среды для запуска автотестов

Для запуска тестов необходимо установить python 3.8

Загрузить библиотеку selenium
```
> pip install selenium
```
Загрузить веб дравер для используемого браузера. (сейчас тесты настроены на хром). Версия веб драйвера должна соответствовать версии браузера.
Прописать путь до директории с веб драйвером в переменную PATH

Автотесты запускаются с учетом переменной окружения для смены адреса сервера "preprod" или "hotfix". По умолчанию запуск будет на сервере test.