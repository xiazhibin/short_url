from fabric.contrib.files import *
from fabric.api import *
from fabric.utils import warn, fastprint
from fabric.colors import *


def update_project():
    if not exists(env.deploy_to):
        with(run(env.projects_folder)):
            warn(red('cloning project'))
            run('git clone git@github.com:xiazhibin/short_url.git')
            warn(red('cloned project'))

    with(cd(env.deploy_to)):
        warn(red('updating project'))
        run('git pull')
        warn(red('updated project'))
        fastprint(green('project ready'), end='\n')
