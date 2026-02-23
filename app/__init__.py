from flask import Flask
from .config import Config
from .extensions import db
from .routes import bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        # Create tables if they don't exist yet
        db.create_all()

    app.register_blueprint(bp)

    return app