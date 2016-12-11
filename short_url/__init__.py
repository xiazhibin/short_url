from flask_redis import FlaskRedis
from flask import Flask, request, redirect, Blueprint

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.url_map.strict_slashes = False
redis_store = FlaskRedis(app)

from short_url.views import mod

app.register_blueprint(mod)
