import re
from collections import namedtuple

PatternsRepl = namedtuple('PatternsRepl', 'pattern, repl')

GMAIL = 'gmail.com'
YANDEX = 'yandex.ru'
MAIL = 'mail.ru'

DEFAULT_DOMAIN = GMAIL

DOMAINS = {
    GMAIL: PatternsRepl(r'([^.!?]*offer[^.]*\.)', ''),
    YANDEX: PatternsRepl(r'<img.*?src="(.+)"[^\>]+>', r'\1'),
    MAIL: PatternsRepl(r'(<img.*?src=".+)\.gif("[^\>]+>)', r'\1.png\2')
}


def filter_content(domain, content):
    pattern = DOMAINS.get(domain, DEFAULT_DOMAIN).pattern
    repl = DOMAINS.get(domain, DEFAULT_DOMAIN).repl
    # print('pattern: ', pattern, 'repl: ', repl)
    return re.sub(pattern, repl, content)

