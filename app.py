from flask import Flask
from config import Config
from controller import bp

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
