# -*- coding: utf-8 -*-
import unittest

from pyramid import testing

from work4la.views import home


class HomeTest(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_view(self):
        request = testing.DummyRequest()
        self.assertEqual(home(request), {})


class HomeFunctionalTest(unittest.TestCase):

    def setUp(self):
        from work4la import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'Work For LA' in res.body)


if __name__ == '__main__':
    unittest.main()
