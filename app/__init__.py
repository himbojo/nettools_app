from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():
    app = Flask(__name__)

    # Import and register routes
    from .routes import init_routes
    init_routes(app)

    # Initialize Socket.IO
    socketio.init_app(app)
    return app
