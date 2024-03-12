from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to The Virtual Pet Adoption Platform"

if __name__ == '__main__':
    app.run(debug=true)