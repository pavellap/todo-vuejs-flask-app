from flask import Flask
app = Flask(__name__)


@app.route('/', methods=['GET'])
def flask_mongodb_atlas():
    return "flask mongo"


if __name__ == "__main__":
    app.run(port=5000, debug=True)