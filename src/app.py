from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<title>Test</title>Hello, Vaibhav!2"

if __name__ == "__main__":
    app.run
