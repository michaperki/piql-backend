from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os 

# Create a Flask application instance
app = Flask(__name__)

# Configuration (You can use environment variables for sensitive data)
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

# Initialize SQLAlchemy for database operations
db = SQLAlchemy(app)

# Import and register blueprints
from routes.auth import auth_bp

app.register_blueprint(auth_bp, url_prefix='/auth')  # Adjust the URL prefix as needed

# Additional configuration and extensions can be added here

if __name__ == '__main__':
    # Use the port specified by Heroku or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)