from flask import Flask, jsonify
from flask_cors import CORS
import logging
from loader import load_ebpf_program
from activity import generate_activity, stop_activity
import threading

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the eBPF program using the loader
bpf = load_ebpf_program()

# Thread to run the activity
activity_thread = None

@app.route('/')
def index():
    return "Welcome to the eBPF Metrics Dashboard!"

# Flask route to expose metrics
@app.route('/metrics', methods=['GET'])
def get_metrics():
    metrics = []
    # Read data from the BPF map (metrics_map)
    for key, value in bpf["metrics_map"].items():
        metrics.append({"pid": key.value, "count": value.value})
    return jsonify(metrics)

@app.route('/generate-activity', methods=['POST'])
def start_activity():
    global activity_thread
    if activity_thread and activity_thread.is_alive():
        return jsonify({"message": "Activity is already running."}), 400

    # Start the activity in a separate thread
    activity_thread = threading.Thread(target=generate_activity)
    activity_thread.start()
    return jsonify({"message": "Activity generation started."}), 200

@app.route('/stop-activity', methods=['POST'])
def stop_activity_endpoint():
    stop_activity()
    return jsonify({"message": "Activity generation stopped."}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)