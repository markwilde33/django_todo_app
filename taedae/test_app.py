from django.apps import apps
from django.test import TestCase
from .apps import TaedaeConfig


class TestTaedaeConfig(TestCase):

    def test_app(self):
        self.assertEqual("taedae", TaedaeConfig.name)
        self.assertEqual("taedae", apps.get_app_config("taedae").name)