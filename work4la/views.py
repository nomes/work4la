# -*- coding: utf-8 -*-
import colander
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound

from work4la.components.job import get_job_by_alias
from work4la.forms import SubscribeSchema


@view_config(route_name='home', renderer='templates/home.jinja2')
def home(request):
    return {}


@view_config(route_name='job', renderer='templates/job_details.jinja2')
def view_job(request):
    job_alias = request.matchdict['job_alias']
    job = get_job_by_alias(job_alias)

    if job is None:
        raise HTTPNotFound()

    return { 'job': job }


@view_config(route_name='subscribe', request_method='POST', renderer='json')
def subscribe(request):
    # TODO(#2):
    # + record subscription and return user-friendly msg
    schema = SubscribeSchema()
    try:
        params = schema.deserialize(request.POST)
    except colander.Invalid as e:
        response = {'success': False}
        response.update(e.asdict())
        return response

    email = params['email']
    job_id = params['job_id']
    return {'success': True, 'email': email, 'job_id': job_id}
