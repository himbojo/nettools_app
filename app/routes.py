from flask import render_template
from flask_socketio import emit
from .utils import validate_hostname, run_ping, run_dig
from . import socketio

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @socketio.on('run_command')
    def handle_command(data):
        command = data.get('command')
        hostname = data.get('hostname')
        options = data.get('options', {})

        if not validate_hostname(hostname):
            emit('output', {'error': 'Invalid hostname or IP'})
            return

        try:
            if command == 'ping':
                count = options.get('count', 4)
                equivalent_command = f"ping -c {count} {hostname}"
                output = f"$ {equivalent_command}\n" + run_ping(hostname, count)
            elif command == 'dig':
                record = options.get('record', 'A')
                if record == "PTR":
                    equivalent_command = f"dig -x {hostname}"
                else:
                    equivalent_command = f"dig {record} {hostname}"
                output = f"$ {equivalent_command}\n" + run_dig(hostname, record)
            else:
                output = "Unsupported command."

            emit('output', {'data': output})
        except Exception as e:
            emit('output', {'error': str(e)})
