from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound

from work4la.components.job import get_job_by_id


@view_config(route_name='home', renderer='templates/home.jinja2')
def home(request):
    return {}


@view_config(route_name='job', renderer='templates/job_details.jinja2')
def view_job(request):
    job_id = request.matchdict['job_id']
    job = get_job_by_id(job_id)

    if job is None:
        raise HTTPNotFound()

    return { 'job': job }


@view_config(route_name='subscribe', request_method='POST', renderer='json')
def subscribe(request):
    # TODO(#2):
    # + validate request params
    # + record subscription and return user-friendly msg
    email = request.params['email']
    job_id = int(request.params['job_id'])
    return {'success': True, 'email': email, 'job_id': job_id}
