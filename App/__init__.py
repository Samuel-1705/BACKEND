from flask import Flask

from config import Config

from .routes.route_users import bp_users
from .routes.route_servers import bp_servers
from .routes.route_channels import bp_channels
from .routes.route_messages import bp_messages
from flask_cors import CORS

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    CORS(app, supports_credentials=True)

    app.config.from_object(Config)
    
    app.register_blueprint(bp_users, url_prefix = '/users')
    app.register_blueprint(bp_servers, url_prefix = '/servers')
    app.register_blueprint(bp_channels, url_prefix = '/channels')
    app.register_blueprint(bp_messages, url_prefix = '/messages')
    return app
