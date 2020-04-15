from django.test import TestCase


class TestTestCase(TestCase):
    def test_sth(self):
        var = "zar"
        self.assertEqual("parsa", var)
