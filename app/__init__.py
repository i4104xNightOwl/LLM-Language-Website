from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Đăng ký các blueprint
    from app.routes import main
    app.register_blueprint(main.bp)

    return app 