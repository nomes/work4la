# -*- coding: utf-8 -*-
import unittest

from work4la.components.job import get_job_by_alias


class GetJobByAliasTestCase(unittest.TestCase):

    def test_alias_not_found(self):
        job = get_job_by_alias('foo')
        self.assertEqual(job, None)

    def test_simple_get(self):
        job = get_job_by_alias('chief-of-airport-planning')
        self.assertEqual(job['alias'], 'chief-of-airport-planning')
        self.assertEqual(job['id'], 1)


if __name__ == '__main__':
    unittest.main()
