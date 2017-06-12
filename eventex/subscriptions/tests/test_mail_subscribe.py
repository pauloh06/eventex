from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="Paulo Henrique", cpf='12345678901', email='paulo.henrique06@hotmail.com', phone='61-98202-7270')
        self.resp = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'paulo.henrique06@hotmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Paulo Henrique',
            '12345678901',
            'paulo.henrique06@hotmail.com',
            '61-98202-7270'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
