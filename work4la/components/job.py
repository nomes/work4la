# -*- coding: utf-8 -*-


# FIXME: Sample data just for development. Later, this should be loaded from
# some kind of storage.
SAMPLE_JOB = {
    'class_code': 7945,
    'classspec_id': 741268,
    'id': 1,
    'alias': 'chief-of-airport-planning',
    'title': 'Chief of Airport Planning',
    'category': 'Architecture and Engineering',
    'salary_low': 60000,
    'salary_high': 80000,
    'department': 'LAWA',
    'min_experience_level': 3,
    'experience_details': 'Two years in planning or related field.',
    'drivers_license': 'standard',
    'exam_type': 'written',
    'exam_date': '2017/09/23',
    'physical_requirements': 2,
    'edu_degree': 3,
    'edu_details': 'Four-year degree in operations management or related field.',
    'certification': None,
    'job_description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis hendrerit massa id congue iaculis. Vivamus bibendum eleifend semper. Pellentesque vitae nulla velit. Morbi ac viverra ligula. Pellentesque non odio ligula. Curabitur massa nunc, lacinia blandit odio sodales, hendrerit ornare neque.'
}

DB = {'chief-of-airport-planning': SAMPLE_JOB}


def get_job_by_alias(job_alias):
    """Main getter for job details."""
    if job_alias not in DB:
        return None
    return DB[job_alias]
