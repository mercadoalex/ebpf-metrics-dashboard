from bcc import BPF
from flask import Flask, jsonify

app = Flask(__name__)

# Load the compiled eBPF program
def load_ebpf_program():
    # Load the eBPF program from the compiled .c file
    bpf = BPF(src_file="/ebpf/metrics.c")

    # Attach the eBPF program to the sched_switch tracepoint
    bpf.attach_tracepoint(tp="sched:sched_switch", fn_name="trace_sched_switch")

    # Return the BPF instance for further use
    return bpf

bpf = load_ebpf_program()

# Flask route to expose metrics
@app.route('/metrics', methods=['GET'])
def get_metrics():
    metrics = []
    for key, value in bpf["metrics_map"].items():
        metrics.append({"pid": key.value, "count": value.value})
    return jsonify(metrics)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)