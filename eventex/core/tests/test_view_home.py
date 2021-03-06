from django.test import TestCase
from django.shortcuts import resolve_url as r

# Create your tests here.
class HomeTest(TestCase):
    fixtures = ['keynotes.json']

    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, '')

    def test_speakers(self):
        """Must show keynote speakers"""
        content = [
            'href="{}"'.format(r('speaker_detail', slug='grace-hopper')),
            'Grace Hopper',
            'http://hbn.link/hopper-pic',
            'href="{}"'.format(r('speaker_detail', slug='alan-turing')),
            'Alan Turing',
            'http://hbn.link/turing-pic',
        ]

        for expected in content:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_shortcuts_links(self):
        """Must show shortcuts link on the header"""
        content = [
            'href="{}#overview"'.format(r('home')),
            'href="{}#speakers"'.format(r('home')),
            'href="{}#sponsors"'.format(r('home')),
            'href="{}#register"'.format(r('home')),
            'href="{}#venue"'.format(r('home')),
        ]

        for expected in content:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_talks_link(self):
        expected = 'href="{}"'.format(r('talk_list'))
        self.assertContains(self.response, expected)
