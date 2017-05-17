# -*- coding: utf-8 -*-
import unittest

from pyramid import testing

from work4la.views import view_job


class JobFunctionalTest(unittest.TestCase):

    def setUp(self):
        from work4la import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_no_id_provided(self):
        res = self.testapp.get('/job/foo', status=404)

    def test_simple_view(self):
        res = self.testapp.get('/job/chief-of-airport-planning', status=200)
        self.assertTrue(b'Chief of Airport Planning' in res.body)


if __name__ == '__main__':
    unittest.main()
