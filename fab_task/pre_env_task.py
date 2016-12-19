from fabric.contrib.files import *
from fabric.api import *
from fabric.utils import warn, fastprint
from fabric.colors import *


def pre_env():
    _pre_system()
    _pre_pyenv()
    _pre_python()
    _pre_pip()
    _pre_pyenv()


def _pre_system():
    sudo('apt-get install -y --force-yes libpq-dev python-dev')
    fastprint(green('system ready'), end='\n')


def _pre_pyenv():
    if exists(env.pyenv_root):
        fastprint(green('pyenv ready'), end='\n')
    else:
        sudo(
            'apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils')
        warn(red('install pyenv'))
        run('git clone https://github.com/yyuu/pyenv.git {0}'.format(env.pyenv_roor))
        run('git clone https://github.com/yyuu/pyenv-virtualenv.git {0}/plugins/pyenv-virtualenv'.format(
            env.pyenv_root))
        warn(red('installed pyenv'))
        fastprint(green('pyenv ready'), end='\n')


def _pre_folder():
    run("mkdir -p {0}".format(env.some_folder_name))
    fastprint('folders ready', end='\n')


def _pre_python():
    if exists(env.python_basic_root):
        fastprint(green('python {0} ready'.format(env.python_version)), end='\n')
    else:
        warn(red('installing python {0}'.format(env.python_version)))
        if exists('$HOME/.pyenv/cache/Python-{0}.tar.xz'.format(env.python_version)):
            run('rm $HOME/.pyenv/cache/Python-{0}.tar.xz'.format(env.python_version))
        run(
            'wget http://mirrors.sohu.com/python/{0}/Python-{0}.tar.xz -q -P $HOME/.pyenv/cache/; {1} install #{fetch(:python_version)}'.format(
                env.python_version, env.pyenv_cmd))
        run('{0} global {1}'.format(env.pyenv_cmd, env.python_version))
        warn(red('installed python {0}'.format(env.python_version)))
        fastprint(green('python {0} ready'.format(env.python_version)), end='\n')


def _pre_pip():
    pip_version = run('{0} --version'.format(env.pip_basic_cmd)).split(' ')[1]
    if pip_version >= env.pip_version:
        fastprint(green('pip ready'), end='\n')
    else:
        warn(red('installing pip'))
        run('{0} install --upgrade pip'.format(env.pip_basic_cmd))
        warn(red('upgraded pip'))
        fastprint(green('pip ready'), end='\n')


def _pre_venv():
    if exists(env.python_venv_root):
        fastprint(green('python virtualenv {0} ready'.format(env.application_name)), end='\n')
    else:
        warn(red('installing python virtualenv {0}'.format(env.application_name)))
        run('{0} virtualenv {1}'.format(env.pyenv_cmd, env.application_name))
        warn(red('installed python virtualenv {0}'.format(env.application_name)))
        fastprint(green('python virtualenv {0} ready'.format(env.application_name)), end='\n')
