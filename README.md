Страница на основе Джанго Рест Апи для учета заказов, сроков поставок, а также их стоимости в рублях и долларах по курсу ЦБРФ. Синхронизация с БД SQLite3. 

Доступ к добавлению и изменению записей есть только у авторизованных пользователей.
Вносится номер заказа, его стоимость в долларах и дата поставки. Поле с рублевой стоимостью можно не заполнять- она автоматически посчитается.
Приложение проверяет, есть ли в базе нужный курс валюты на дату поставки.
Если да- по нему рассчитывается рублевая стоимость заказа и добавляется в таблицу. 
Если нет- считывает на указанную дату курс валюты с сайта ЦБРФ. Если на сайте еще нет курса на такую дату- подставляется курс за сегодня. 
