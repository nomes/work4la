from pyramid.view import view_config


from work4la.components.job import get_job_by_id


@view_config(route_name='home', renderer='templates/home.jinja2')
def home(request):
    return {}


@view_config(route_name='job', renderer='templates/job_details.jinja2')
def view_job(request):
    job = get_job_by_id(1)
    return { 'job': job }
