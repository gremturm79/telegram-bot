Бот отправляет 3 анекдота подряд, каждые 6 часов, что можно изменить в самом коде scheduler.add_job(send_message_time, 'interval', hours=6, kwargs={'bot': bot}, поменяв в параметре hours значение, установив необходимое время оправки.
Запускается файлом bot_send_anekdot.py
необходимые зависимости в файле requirements.txt
для связи email: gremturm@gmail.com
