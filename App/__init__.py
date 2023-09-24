from flask import Flask

from config import Config

from .routes.route_users import bp_users


from flask_cors import CORS

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    CORS(app, supports_credentials=True)

    app.config.from_object(Config)
    
    app.register_blueprint(bp_users, url_prefix = '/users')
    app.register_blueprint(bp_users, url_prefix = '/servers')
    app.register_blueprint(bp_users, url_prefix = '/messages')
    app.register_blueprint(bp_users, url_prefix = '/channels')

    return app