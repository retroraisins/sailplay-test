# Тестовое задание для python-разработчика. API для отправки Email

В коде приложения хотим уметь удобно (для разработчиков) отправлять письма, не думая о том, как внутри работает отправка письма и фильтрация контента.

Отправка письма происходит через внутренний сервис по HTTP API:

https://email-machine.internal/api/email-gate/{email-domain}/ 

(в рамках тестового задания **не нужно** делать сам сервис отправки),

где email-domain может быть:
- gmail
- yandex
- mail

Если домен получателя не входит в список, использовать по умолчанию gmail.

Формат JSON запроса отправки письма через сервис:
```
{
    "email: "test@domain.com",
    "content": "email content"
}
```

### Фильтрация контента.

Если домен получателя:
- gmail.com: удаляем все предложения, которые содержат слово `offer`.
- yandex.ru: заменяем все картинки текстом ссылки на картинку, т.е. `<img src="https://spam.org/pic1.png"/>` => `https://spam.org/pic1.png`
- mail.ru: заменяем у всех изображений расширение файла с gif на png, т.е. `<img src="https://spam.org/pic1.gif" />` => `<img src="https://spam.org/pic1.png" />`

### Хотим получить:
1) Единую точку входа для отправки письма.
2) Расширяемость на уровне правил фильтрации контента, т.к. правила часто дополняются, и их может быть больше чем одно.
3) Расширяемость на уровне почтовых клиентов, т.к. список клиентов растет.


### Ожидаем, что пользоваться API можно будет:

```
from messaging.email import Email

email = Email('test1@gmail.com', 'Hello gmail! I have an offer for you.')
email.send()
>>> {'email': "test1@gmail.com", 'Hello gmail!'}

email = Email('test2@yandex.ru', 'Hello yandex! I have an pic <img src="https://spam.org/pic1.png" /> for you.')
email.send()
>>> {'email': "test2@yandex.ru", 'Hello yandex! I have an pic https://spam.org/pic1.png for you.'}

email = Email('test3@mail.ru', 'Hello mail! I have an pic <img src="https://spam.org/pic1.gif" /> for you.')
email.send()
>>> {'email': 'test3@mail.ru', 'Hello mail! I have an pic <img src="https://spam.org/pic1.png" /> for you.'}

email = Email('test4@sailplay.ru', 'Hello another mail client! I have an offer for you.')
email.send()
>>> {'email': 'test4@sailplay.ru', 'Hello another mail client!'}
```

Реализацию задания выложить в репозиторий и предоставить ссылку.

