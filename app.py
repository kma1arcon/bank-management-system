from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Banking API is running"

@app.route("/balance")
def balance():
    return "Your balance is 1000"

@app.route("/hello")
def hello():
    return "Hello, John Doe!"

if __name__ == "__main__":
    app.run(debug=True) 