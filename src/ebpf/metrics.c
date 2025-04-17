#include <linux/bpf.h>
#include <linux/ptrace.h>
#include <linux/sched.h>
#include <linux/version.h>
#include <bpf/bpf_helpers.h>

// Define a structure to hold CPU and memory usage metrics
struct metrics {
    __u64 cpu_usage;      // Placeholder for CPU usage (currently using PID)
    __u64 memory_usage;   // Placeholder for memory usage (currently using UID)
};

// Define a structure to hold metrics along with a timestamp
struct metrics_data {
    struct metrics metrics;  // The metrics (CPU and memory usage)
    __u64 timestamp;         // Timestamp of when the metrics were collected
};

// Define a BPF map to send data to user space via a perf event array
struct bpf_map_def SEC("maps/metrics_map") metrics_map = {
    .type = BPF_MAP_TYPE_PERF_EVENT_ARRAY,  // Map type for perf event output
    .max_entries = 1,                      // Maximum number of entries in the map
};

// Attach this eBPF program to the "sched_switch" tracepoint
SEC("tracepoint/sched/sched_switch")
int trace_sched_switch(struct trace_event_raw_sched_switch *ctx) {
    struct metrics_data data = {};  // Initialize a local structure to hold metrics data
    
    // Collect CPU usage and memory usage metrics
    data.metrics.cpu_usage = bpf_get_current_pid_tgid(); // Get the current process ID (placeholder for CPU usage)
    data.metrics.memory_usage = bpf_get_current_uid_gid(); // Get the current user ID (placeholder for memory usage)
    data.timestamp = bpf_ktime_get_ns(); // Get the current kernel time in nanoseconds

    // Send the collected data to the perf event map for user-space consumption
    bpf_perf_event_output(ctx, &metrics_map, BPF_F_CURRENT_CPU, &data, sizeof(data));
    return 0; // Return 0 to indicate successful execution
}

// Specify the license of the eBPF program (required by the kernel)
char LICENSE[] SEC("license") = "GPL";