# -*- coding: utf-8 -*-
import json
import unittest

from pyramid import testing

from work4la.views import subscribe


class SubscribeFunctionalTest(unittest.TestCase):

    def setUp(self):
        from work4la import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_get_404s(self):
        self.testapp.get('/subscribe', status=404)

    def test_subscribe(self):
        response = self.testapp.post(
            '/subscribe',
            {'email': 'alex@work4.la', 'job_id': 1})
        self.assertEqual(
            response.json_body,
            {'success': True, 'email': 'alex@work4.la', 'job_id': 1})


if __name__ == '__main__':
    unittest.main()
