from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application instance
app = Flask(__name__)

# Configuration (You can use environment variables for sensitive data)
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your-database-file.db'  # Use SQLite for simplicity

# Initialize SQLAlchemy for database operations
db = SQLAlchemy(app)

# Import and register blueprints
from routes.auth import auth_bp

app.register_blueprint(auth_bp, url_prefix='/auth')  # Adjust the URL prefix as needed

# Additional configuration and extensions can be added here

if __name__ == '__main__':
    app.run()
