# -*- coding: utf-8 -*-
import unittest

from work4la.test.util.app_test_case import AppTestCase
from work4la.views import subscribe


class SubscribeFunctionalTest(AppTestCase):

    def test_get_404s(self):
        self.testapp.get('/subscribe', status=404)

    def test_subscribe(self):
        self._assert_response_for_request(
            {'email': 'alex@workfor.la', 'job_id': 1},
            {'success': True, 'email': 'alex@workfor.la', 'job_id': 1})

    def test_missing_email_parameter(self):
        self._assert_response_for_request(
            {'job_id': 1},
            {'success': False, 'email': 'Required'})

        self._assert_response_for_request(
            {'job_id': 1, 'email': ''},
            {'success': False, 'email': 'Required'})

    def test_missing_job_id_parameter(self):
        self._assert_response_for_request(
            {'email': 'alex@workfor.la'},
            {'success': False, 'job_id': 'Required'})

    def test_bad_email(self):
        self._assert_response_for_request(
            {'email': 'workfor.la', 'job_id': 1},
            {'success': False, 'email': 'Invalid email address'})

    def _assert_response_for_request(self, request_json, expected_response):
        response = self.testapp.post('/subscribe', request_json)
        self.assertEqual(response.json_body, expected_response)


if __name__ == '__main__':
    unittest.main()
