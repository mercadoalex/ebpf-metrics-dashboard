const fetchMetrics = async () => {
    try {
        const response = await fetch('/api/metrics');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const metrics = await response.json();
        updateMetricsUI(metrics);
    } catch (error) {
        console.error('Error fetching metrics:', error);
    }
};

const fetchLogs = async () => {
    try {
        const response = await fetch('/api/logs');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const logs = await response.json();
        updateLogsUI(logs);
    } catch (error) {
        console.error('Error fetching logs:', error);
    }
};

const updateMetricsUI = (metrics) => {
    const metricsContainer = document.getElementById('metrics');
    metricsContainer.innerHTML = JSON.stringify(metrics, null, 2);
};

const updateLogsUI = (logs) => {
    const logsContainer = document.getElementById('logs');
    logsContainer.innerHTML = logs.map(log => `<div>${log}</div>`).join('');
};

document.addEventListener('DOMContentLoaded', () => {
    fetchMetrics();
    fetchLogs();
    setInterval(() => {
        fetchMetrics();
        fetchLogs();
    }, 5000); // Refresh every 5 seconds
});