from flask import Blueprint, jsonify
import subprocess

routes = Blueprint('routes', __name__)

@routes.route('/metrics', methods=['GET'])
def get_metrics():
    try:
        # Call the eBPF program to get metrics
        metrics = subprocess.check_output(['bpftool', 'map', 'dump', 'id', 'YOUR_METRICS_MAP_ID'])
        return jsonify({'metrics': metrics.decode('utf-8')}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@routes.route('/logs', methods=['GET'])
def get_logs():
    try:
        # Call the eBPF program to get logs
        logs = subprocess.check_output(['bpftool', 'prog', 'dump', 'id', 'YOUR_LOGS_PROG_ID'])
        return jsonify({'logs': logs.decode('utf-8')}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500