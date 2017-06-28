# -*- coding: utf-8 -*-
import unittest

from work4la.test.util.db import TEST_DB_URL


class AppTestCase(unittest.TestCase):

    def setUp(self):
        settings = {
            'sqlalchemy.url': TEST_DB_URL
        }
        from work4la import main
        app = main({}, **settings)
        from webtest import TestApp
        self.testapp = TestApp(app)
