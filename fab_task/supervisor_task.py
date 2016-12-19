from fabric.contrib.files import *
from fabric.api import *
from fabric.utils import warn, fastprint
from fabric.colors import *


@task
def supervisor_status():
    sudo('supervisorctl -c /etc/supervisor/supervisord.conf status')
