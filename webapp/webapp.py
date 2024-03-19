import mysql.connector
from flask import Flask

app = Flask(__name__)

# Database connection parameters
db_config = {
    'host': 'your-rds-host.amazonaws.com',
    'user': 'your-master-username',
    'password': 'your-password',
    'database': 'your-database-name'
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
