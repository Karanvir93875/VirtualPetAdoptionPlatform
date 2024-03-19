import mysql.connector
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

# Database connection parameters
db_config = {
    'host': 'petpaldb1.cd2oqkeq6cy3.us-east-1.rds.amazonaws.com',
    'user': 'petpaldb',
    'password': '',
    'database': ''
}

# Establishing a connection to the MySQL database
try:
    conn = mysql.connector.connect(**db_config)
    print("Connection to MySQL database successful")
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")

@app.route('/')
def home():
    return "Welcome to PetPal Virtual Adoption Platform!"

if __name__ == '__main__':
    app.run(debug=True)

# Initialize SQLAlchemy with no settings
db = SQLAlchemy()

    # Configuration settings for application, for example:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost/petpal'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    # Import and register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    

    
    return app
