# -*- coding: utf-8 -*-
import unittest

from sqlalchemy import create_engine

from work4la.components import exam_subscription
from work4la.models import ExamSubscriptionModel
from work4la.models import DBSession
from work4la.test.util.db import TEST_DB_URL



class ExamSubscriptionTestCase(unittest.TestCase):

    # TODO: move database configuration and helpers someplace
    # sharable so this file has no DB-related imports
    @classmethod
    def setUpClass(cls):
        engine = create_engine(TEST_DB_URL)
        DBSession.configure(bind=engine)

    def tearDown(self):
        DBSession.rollback()

    def test_make_new(self):
        new_es = exam_subscription.make_new('test@email.com', 120)
        self.assertIsNotNone(new_es.id)
        self.assertEqual(new_es.email_address, 'test@email.com')
        self.assertEqual(new_es.job_id, 120)
        self.assertIsNone(new_es.time_sent)

        db_es = DBSession.query(ExamSubscriptionModel)\
             .filter(ExamSubscriptionModel.id == new_es.id)\
             .one()
        self.assertEqual(db_es.email_address, new_es.email_address)
        self.assertEqual(db_es.job_id, new_es.job_id)
        self.assertEqual(db_es.id, new_es.id)


if __name__ == '__main__':
    unittest.main()
