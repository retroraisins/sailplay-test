from email import Email


email = Email('test1@gmail.com', 'Hello gmail! I have an offer for you.')
assert email.send() == {'email': 'test1@gmail.com', 'content': 'Hello gmail!'}, 'Case 1 failed'

email = Email('test2@yandex.ru', 'Hello yandex! I have an pic <img src="https://spam.org/pic1.png" /> for you.')
assert email.send() == {'email': "test2@yandex.ru", 'content': 'Hello yandex! I have an pic https://spam.org/pic1.png for you.'}, 'Case 2 failed'

email = Email('test3@mail.ru', 'Hello mail! I have an pic <img src="https://spam.org/pic1.gif" /> for you.')
assert email.send() == {'email': 'test3@mail.ru', 'content': 'Hello mail! I have an pic <img src="https://spam.org/pic1.png" /> for you.'}, 'Case 3 failed'

email = Email('test4@sailplay.ru', 'Hello another mail client! I have an offer for you.')
assert email.send() == {'email': 'test4@sailplay.ru', 'content': 'Hello another mail client!'}, 'Case 4 failed'

print('Looks good!')