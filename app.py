from flask import Flask
from controller.radar_controller import bp

app = Flask(__name__)
app.register_blueprint(bp)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()