# -*- coding: utf-8 -*-
import unittest

from pyramid import testing

from work4la.views import view_job


class HomeTest(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_view(self):
        request = testing.DummyRequest()
        view_job_data = view_job(request)
        self.assertEqual(
            view_job_data['job']['id'],
            'chief-of-airport-planning')


class HomeFunctionalTest(unittest.TestCase):

    def setUp(self):
        from work4la import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/job', status=200)
        self.assertTrue(b'Chief of Airport Planning' in res.body)


if __name__ == '__main__':
    unittest.main()
