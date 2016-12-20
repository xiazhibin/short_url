from fabric.contrib.files import *
from fabric.api import *
from fabric.utils import warn, fastprint
from fabric.colors import *


@task
def supervisor_status():
    sudo('supervisorctl -c /etc/supervisor/supervisord.conf status')


@task
def upload_supervisor_config():
    file_name = '{0}/{1}'.format(env.supervisor_config_path, env.supervisor_config_name)
    if exists(file_name):
        sudo('rm {0}'.format(file_name))
    put(env.supervisor_config_name, env.supervisor_config_path, use_sudo=True)
    fastprint(green('supervisor config ready'), end='\n')


@task()
def stop_app():
    if not env.get('supervisor_role'):
        env.supervisor_role = prompt("which app?|(all,app name)")
    sudo('supervisorctl -c /etc/supervisor/supervisord.conf stop {0}'.format(env.supervisor_role))


@task
def start_app():
    if not env.get('supervisor_role'):
        env.supervisor_role = prompt("which?|(self, all,app name)")
    if env.supervisor_role == 'self':
        sudo('supervisord -c /etc/supervisor/supervisord.conf')
    else:
        sudo('supervisorctl -c /etc/supervisor/supervisord.conf start {0}'.format(env.supervisor_role))


@task
def reload_suprevisor():
    sudo('supervisorctl -c /etc/supervisor/supervisord.conf reload')
    set_supervisor_role('all')
    execute(start_app)


def set_supervisor_role(role=None):
    if not role:
        role = env.application_name
    env.supervisor_role = role
