from django.test import TestCase


class TestTestCase(TestCase):
    def test_sth(self):
        var = "parsa"
        self.assertEqual("parsa", var)
