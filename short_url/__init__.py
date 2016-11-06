from flask_redis import FlaskRedis
from flask import Flask, request, redirect
from datetime import datetime, timedelta
import urllib2

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.url_map.strict_slashes = False
redis_store = FlaskRedis(app)


@app.route('/', methods=['POST'])
def shorten():
    url = request.form.get('url')
    if not pre_check(url):
        return 'url is not accessable'
    from number_sender import get_number
    short_url = redis_store.get(url)
    if short_url is None:
        short_url = get_number()
        redis_store.set(short_url, url)
        redis_store.set(url, short_url)
    expire_time = datetime.now() + timedelta(seconds=app.config['EXPIRE_TIME_DELTA'])
    redis_store.expireat(url, expire_time)
    return 'http://{0}/{1}'.format(app.config['YOUR_HOST'], short_url)


@app.route('/<path:url>')
def recovery_url(url):
    rv = redis_store.get(url)
    if rv is not None:
        return redirect(rv, code=302)
    else:
        return 'error'


def pre_check(url):
    rv = False
    try:
        response = urllib2.urlopen(url, timeout=3)
        if response.getcode() == 200:
            rv = True
    except Exception:
        rv = False
    return rv
