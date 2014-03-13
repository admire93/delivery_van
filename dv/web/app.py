from flask import Flask

from . import facebook_login
from .facebook_login import oauth
from ..db import session, ensure_shutdown_session

app = Flask(__name__)

app.register_blueprint(facebook_login.bp, url_prefix='/fb')

oauth.init_app(app)

ensure_shutdown_session(app)
