# -*- coding: utf-8 -*-
import unittest


from work4la.components.job import get_job_by_id


class GetJobByIdTestCase(unittest.TestCase):

    def test_id_not_found(self):
        job = get_job_by_id(1)
        self.assertEqual(job, None)

    def test_simple_get(self):
        job = get_job_by_id('chief-of-airport-planning')
        self.assertEqual(job['id'], 'chief-of-airport-planning')


if __name__ == '__main__':
    unittest.main()
