from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<title>Application</title>Hello, Rohit!"

if __name__ == "__main__":
    app.run
