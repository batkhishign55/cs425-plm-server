from flask import Blueprint, render_template

from protect import adminProtect

from .controller import logController

log = Blueprint(
    'log', __name__, static_folder='static', template_folder='templates',
    url_prefix='/log'
)


@log.before_request
@adminProtect
def login_required():
    pass


@log.get('/<log_id>')
def index(log_id):
    return render_template('log.html')


@log.get('/api/')
def logList():
    return logController().get()


@log.get('/api/detail/<log_id>')
def logDetail(log_id):
    return logController().getSinglelog(log_id)
