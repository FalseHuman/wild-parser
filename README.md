# Wildberries парсер

## Установка geckodriver в Ubuntu, Debian и ArchLinux
``` bash
#Вытаскиваем файл из архива.
$ tar -xvzf geckodriver*
#Даем нужные права драйверу.
$ sudo chmod +x geckodriver
#Отправляем драйвер в папку где его будет искать Selenium.
$ sudo mv geckodriver /usr/local/bin/
```
Ссылка как установить для [других ОС](https://selenium-python.com/install-geckodriver)
## Настройка backend

```bash
#Установите нужные библиотеки
$ cd wildberries
$ pip install -r ./requirements.txt
#Спарсить товары
$ python manage.py parsing_product
#Запуск сервера
$ python manage.py runserver 8001
```
## Настройка frontend

```bash
$ cd frontend/wild-front
$ npm install
$ npm run serve
```
## СУБД PostgreSQL
Ссылка как установить для [Windows](https://www.youtube.com/watch?v=yYJ74Sc7nw8)
Ссылка как установить для [Linux](https://losst.ru/ustanovka-postgresql-ubuntu-16-04)