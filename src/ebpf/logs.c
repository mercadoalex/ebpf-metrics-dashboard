#include <linux/bpf.h>
#include <linux/ptrace.h>
#include <linux/sched.h>
#include <linux/ktime.h>
#include <linux/uio.h>
#include <linux/bpf_helpers.h>

// Define a BPF map to store log entries
struct bpf_map_def SEC("maps/logs_map") logs_map = {
    .type = BPF_MAP_TYPE_ARRAY,  // Array map type to store logs
    .max_entries = 1024,        // Maximum number of log entries
};

// Attach this eBPF program to the "sched_switch" tracepoint
SEC("tracepoint/sched/sched_switch")
int trace_sched_switch(struct trace_event_raw_sched_switch *ctx) {
    char log_entry[256];  // Buffer to store the log message

    // Get the task_struct of the previous and next processes involved in the context switch
    struct task_struct *prev = (struct task_struct *)ctx->prev_pid; // Previous process
    struct task_struct *next = (struct task_struct *)ctx->next_pid; // Next process

    // Format a log message indicating the context switch
    bpf_snprintf(log_entry, sizeof(log_entry), "Switching from %s to %s", prev->comm, next->comm);

    // Store the log message in the logs_map using the tracepoint type as the key
    bpf_map_update_elem(&logs_map, &ctx->common.type, log_entry, BPF_ANY);

    return 0; // Return 0 to indicate successful execution
}

// Specify the license of the eBPF program (required by the kernel)
char _license[] SEC("license") = "GPL";