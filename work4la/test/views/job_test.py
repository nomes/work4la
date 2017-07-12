# -*- coding: utf-8 -*-
import unittest

from work4la.test.util.app_test_case import AppTestCase


class JobFunctionalTest(AppTestCase):

    def test_bad_alias(self):
        res = self.testapp.get('/job/foo', status=404)

    def test_no_alias(self):
        res = self.testapp.get('/job', status=404)

    def test_simple_view(self):
        res = self.testapp.get('/job/chief-of-airport-planning', status=200)
        self.assertTrue(b'Chief of Airport Planning' in res.body)


if __name__ == '__main__':
    unittest.main()
