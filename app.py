from flask import Flask, jsonify, request
import socket

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return "Hello from Dobhal ECS Container"

@app.route('/host', methods=['GET'])
def host():
    hostname = socket.gethostname()
    return f"Hostname: {hostname}"

@app.route('/ip', methods=['GET'])
def ip():
    ip_address = request.remote_addr
    return f"Client IP: {ip_address}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
