import json
import pytest
from unittest import TestCase

from django.test import Client
from django.urls import reverse
from .models import Company

import os
print("Eden is printing PYTHONPATH:")
print(os.environ["PYTHONPATH"])
print("Eden is printing DJANGO_SETTINGS_MODULE:")
print(os.environ["DJANGO_SETTINGS_MODULE"])

class TestGetCompanies(TestCase):
    def test_zero_companies_should_return_empty_list(self) -> None:
        client = Client()
        companies_url = reverse("companies-list")
        response = client.get(companies_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), [])
