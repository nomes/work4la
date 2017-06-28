from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from work4la.models import DBSession


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    # sqlalchemy
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('job', '/job/{job_alias}')
    config.add_route('subscribe', '/subscribe')
    config.scan()
    return config.make_wsgi_app()
