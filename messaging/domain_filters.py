import re

DEFAULT_DOMAIN = 'gmail.com'
DOMAINS = ('gmail.com', 'yandex.ru', 'mail.ru', )


class DomainFilter:
    def __init__(self, domain):
        self._domain = domain
        self.default_filter = self.gmail_filter

    def __call__(self, content):
        if self._domain == 'gmail.com':
            return self.gmail_filter(content)
        elif self._domain == 'yandex.ru':
            return self.yandex_filter(content)
        elif self._domain == 'mail.ru':
            return self.mail_filter(content)
        else:
            return self.default_filter(content)

    def gmail_filter(self, content):
        return re.sub(r'([^.!?]*offer[^.]*\.)', '', content)

    def yandex_filter(self, content):
        return re.sub(r'<img.*?src="(.+)"[^\>]+>', r'\1', content)


    def mail_filter(self, content):
        return re.sub(r'(<img.*?src=".+)\.gif("[^\>]+>)', r'\1.png\2', content)
