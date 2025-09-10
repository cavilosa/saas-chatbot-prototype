# src/__init__.py
from flask import Flask
from .config import Config
from .extensions import oauth

def create_app():
    """Construct the core application."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    oauth.init_app(app)
    
    oauth.register(
        name='auth0',
        client_id=app.config['AUTH0_CLIENT_ID'],
        client_secret=app.config['AUTH0_CLIENT_SECRET'],
        server_metadata_url=f'https://{app.config["AUTH0_DOMAIN"]}/.well-known/openid-configuration',
        client_kwargs={'scope': 'openid profile email'}
    )

    with app.app_context():
        # Import and register Blueprints
        
        from .auth import routes as auth_routes
        from .main import routes as main_routes
        
        app.register_blueprint(auth_routes.auth_bp)
        app.register_blueprint(main_routes.main_bp)

        return app