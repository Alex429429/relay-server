from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)
received_packets = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_packet', methods=['POST'])
def send_packet():
    timestamp = time.time()
    received_packets.append(timestamp)
    print(f"[SERVER] Packet received at {timestamp}")
    return jsonify({'status': 'success', 'received_at': timestamp})

@app.route('/logs')
def logs():
    return jsonify(received_packets)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
