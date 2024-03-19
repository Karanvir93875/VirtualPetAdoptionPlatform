import mysql.connector
from flask import Flask

app = Flask(__name__)

# Database connection parameters
db_config = {
    'host': 'petpaldb1.cd2oqkeq6cy3.us-east-1.rds.amazonaws.com',
    'user': 'petpaldb',
    'password': 'Flameo17',
    'database': 'petpaldb1'
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
