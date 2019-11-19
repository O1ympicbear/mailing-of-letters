import smtplib


recipient_name= ""  #Имя получателя
sender_name= ""  #Имя отправителя
login= ""  #Почтовый ящик отправителя
password= ""  #Пароль почтового ящика отправителя

mailing = """
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. После окончания курса у тебя будет 2 месяца, чтобы догнать программу. 
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""


mailing = mailing.replace('%website%','dvmn.org')
mailing = mailing.replace('%friend_name%', recipient_name)
mailing = mailing.replace('%my_name%', sender_name)
sender_email = input('Введите свою почту: ')
recipient_email = input('Введите почту получателя: ')

sending = """From: {0}
To: {1}
Subject: Проверка!
Content-Type: text/plain; charset="UTF-8";
{2}""".format(sender_email, recipient_email, mailing)

server = smtplib.SMTP_SSL('smtp.yandex.com:465')
server.login(login, password)

server.sendmail(sender_email, recipient_email, sending.encode("UTF-8"))
server.quit()
