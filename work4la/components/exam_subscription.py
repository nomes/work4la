# -*- coding: utf-8 -*-
from collections import namedtuple

from work4la.models import DBSession
from work4la.models import ExamSubscriptionModel


class ExamSubscription(namedtuple('ExamSubscription',
                                  ['id', 'time_created',
                                   'time_sent', 'email_address',
                                   'job_id'])):

    @classmethod
    def from_model(cls, model):
        return cls(model.id, model.time_created, model.time_sent,
                   model.email_address, model.job_id)


def make_new(email_address, job_id):
    """Record a new subscription for exam notifications.

    email_address -- user's email address
    job_id -- ID of job class (not class_code or classspec_id)
    """
    new_subscription = ExamSubscriptionModel(
        email_address=email_address,
        job_id=job_id)
    DBSession.add(new_subscription)
    DBSession.flush()
    return ExamSubscription.from_model(new_subscription)
