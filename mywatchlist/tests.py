# Create your tests here.
from http import client
from django.test import TestCase, Client
from django.urls import reverse
from mywatchlist.models import MyWatchList
# Create your tests here.
class TestViews(TestCase):
    def test_watchlist_HTML(self):
        client = Client()
        response = client.get(reverse('mywatchlist:show_html'))
        self.assertEquals(response.status_code, 200)
    def test_XML(self):
        client = Client()
        response = client.get(reverse('mywatchlist:show_xml'))
        self.assertEquals(response.status_code, 200)
    def test_JSON(self):
        client = Client()
        response = client.get(reverse('mywatchlist:show_json'))
        self.assertEquals(response.status_code, 200)