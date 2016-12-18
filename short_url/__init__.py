from flask import Flask
from flask_redis import FlaskRedis

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
app.secret_key = app.config['SECRET_KEY']
app.url_map.strict_slashes = False
redis_store = FlaskRedis(app)

from short_url.views import mod

app.register_blueprint(mod)
