from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.cve_routes import cve_blueprint

app = Flask(__name__)

# Database configuration (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cve.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Register routes from cve_routes
app.register_blueprint(cve_blueprint)

if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask app in debug mode
