// Start activity
document.getElementById("start-activity").addEventListener("click", () => {
    fetch("/generate-activity", { method: "POST" })
        .then(response => response.json())
        .then(data => console.log(data.message))
        .catch(error => console.error("Error starting activity:", error));
});

// Stop activity
document.getElementById("stop-activity").addEventListener("click", () => {
    fetch("/stop-activity", { method: "POST" })
        .then(response => response.json())
        .then(data => console.log(data.message))
        .catch(error => console.error("Error stopping activity:", error));
});