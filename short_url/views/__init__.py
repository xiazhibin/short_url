from datetime import datetime, timedelta

import requests
from flask import Blueprint, request, redirect, jsonify

from short_url import redis_store, app
from short_url.number_sender import get_number
from short_url.utils.decorators import crossdomain

mod = Blueprint('short_url', __name__, url_prefix='/short_url')
EXPIRE_TIME_DELTA = app.config['EXPIRE_TIME_DELTA']
HOST = app.config['YOUR_HOST']


@mod.route('/', methods=['POST'])
@crossdomain('*')
def shorten():
    url = request.form.get('url')
    if not pre_check(url):
        return jsonify({'data': "url is not accessable"})

    short_url = redis_store.get(url)
    if short_url is None:
        short_url = get_number()
        redis_store.set(short_url, url)
        redis_store.set(url, short_url)
    expire_time = datetime.now() + timedelta(seconds=EXPIRE_TIME_DELTA)
    redis_store.expireat(url, expire_time)

    rv = '{0}{1}/{2}'.format(HOST, mod.url_prefix, short_url)
    return jsonify({'data': rv})


@mod.route('/<path:url>')
def recovery_url(url):
    rv = redis_store.get(url)
    if rv is not None:
        return redirect(rv, code=302)
    else:
        return 'error'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection': 'keep-alive'
}


def pre_check(url):
    rv = False
    try:
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            rv = True
    except Exception as e:
        rv = False
    return rv
