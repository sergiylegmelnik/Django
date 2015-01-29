from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.template import RequestContext
from views import home


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')

        self.assertEqual(found.func, home)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()

        response = home(request)

        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        self.assertIn(b'<title>To-Do</title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))

    def test_home_page_returns_correct_html_content(self):
        request = HttpRequest()
        response = home(request)

        expected_html = render_to_string('home.html', {'title': 'To-Do'})

        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home(request)

        model = {'title': 'To-Do', 'new_item_text': 'A new list item'}
        expected_html = render_to_string('home.html', model, RequestContext(request))
        self.assertEqual(response.content.decode(), expected_html)