from flask import Flask
from controller.radar_controller import bp as radar_bp
from controller.capture_controller import bp as capture_bp

app = Flask(__name__)
app.register_blueprint(radar_bp)
app.register_blueprint(capture_bp)

if __name__ == '__main__':
    app.run()
