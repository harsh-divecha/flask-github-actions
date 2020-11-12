from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return f"<title>Test</title>{get_hello_text('Vaibhav')}!2"

def get_hello_text(name):
    return f'Hello, {name}'
    
if __name__ == "__main__":
    app.run
