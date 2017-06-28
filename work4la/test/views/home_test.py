# -*- coding: utf-8 -*-
import unittest

from pyramid import testing

from work4la.test.util.app_test_case import AppTestCase
from work4la.views import home


class HomeTest(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_view(self):
        request = testing.DummyRequest()
        self.assertEqual(home(request), {})


class HomeFunctionalTest(AppTestCase):

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'Work For LA' in res.body)


if __name__ == '__main__':
    unittest.main()
