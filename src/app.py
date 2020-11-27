from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return f"<title>{get_title()}</title>Hello, Rohit!"

def get_title():
    return 'Application'
if __name__ == "__main__":
    app.run
