from datetime import date
import json
from django.test import TestCase, Client
from chdb_app.models import *


class SearchTestCase(TestCase):
    def setUp(self):
        city = City.objects.create(name='Montross')
        Person.objects.create(
            name='George Washington', born_on=date(1732, 2, 22), born_at=city
        )
        City.objects.create(name='Georgetown')

    def test_search(self):
        client = Client()
        response = client.post('/api/v1/search', {
            'query': 'George',
        })
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.json())

        data = json.loads(response.json())
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['fields']['name'], 'George Washington')
