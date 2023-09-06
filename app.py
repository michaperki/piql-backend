from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.main import main_bp

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load configuration from a config file or environment variables
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

    # Initialize database
    db.init_app(app)

    # Register the main blueprint
    app.register_blueprint(main_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
