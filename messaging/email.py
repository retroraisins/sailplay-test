from domain_filters import DomainFilter, DOMAINS, DEFAULT_DOMAIN
from email_validator import validate_email, EmailNotValidError
import json

# possible import error: there is builtin "email" pkg
class Email:

    def __init__(self, email, content):
        self.email = email
        self.content = content
        self.filter_func = DomainFilter(self.email_domain)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = self._validate_email(value)

    @email.deleter
    def email(self):
        raise AttributeError('Can''t delete attribute')

    @property
    def domain(self):
        return self.email_domain[:self.email_domain.find('.')]

    @property
    def email_domain(self):
        v = validate_email(self.email)
        if v['domain'] not in DOMAINS:
            return DEFAULT_DOMAIN
        return v['domain']

    def _validate_email(self, email):
        try:
            v = validate_email(email)
            return v['email']
        except EmailNotValidError as e:
            raise e

    def send(self):
        url = 'https://email-machine.internal/api/email-gate/%s/' % self.domain
        return {'email': self.email, 'content': self.filtered_content}
        # return json.dumps({'email': self.email, 'content': self.filtered_content})

    @property
    def filtered_content(self):
        return self.filter_func(self.content)
