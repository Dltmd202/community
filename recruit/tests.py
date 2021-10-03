from django.test import TestCase
from .models import *


# Create your tests here.
class TestView(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_tag(self):
        