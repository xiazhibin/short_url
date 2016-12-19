from fabric.api import cd, run, env, hosts, task
from fab_task.pre_env_task import pre_env
from fab_task.update_project_task import update_project

env.hosts = ['xiazhibin@xiazhibin.cn']
env.user = 'xiazhibin'
env.key_filename = "~/.ssh/id_rsa"
env.home = "/home/{0}".format(env.user)
env.application_name = 'short_url'
env.projects_folder = "{0}/projects".format(env.home)
env.deploy_to = "{0}/projects/{1}".format(env.home, env.application_name)
env.pyenv_root = "{0}/.pyenv".format(env.home)
env.pyenv_virtualenv = env.application_name
env.python_version = '2.7.11'
env.pip_version = '8.1.2'
env.pip_system_version = '1.5.4'

env.pyenv_bin_path = "{0}/bin".format(env.pyenv_root)
env.pyenv_cmd = "{0}/pyenv".format(env.pyenv_bin_path)

env.python_basic_root = "{0}/versions/{1}".format(env.pyenv_root, env.python_version)
env.python_basic_bin_path = "{0}/bin".format(env.python_basic_root)
env.python_basic_cmd = "{0}/python".format(env.python_basic_bin_path)
env.pip_basic_cmd = "{0}/pip".format(env.python_basic_bin_path)

env.python_venv_root = "{0}/versions/{1}".format(env.pyenv_root, env.application_name)
env.python_venv_bin_path = "{0}/bin".format(env.python_venv_root)
env.python_venv_cmd = "{0}/python".format(env.python_venv_bin_path)
env.pip_venv_cmd = "{0}/pip".format(env.python_venv_bin_path)


@task
def deploy():
    pre_env()
    update_project()
