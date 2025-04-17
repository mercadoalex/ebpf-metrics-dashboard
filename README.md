# eBPF Metrics Dashboard

This project is an eBPF-based metrics and logging dashboard that collects system metrics and logs, providing a web interface for visualization and monitoring.

## Project Structure

- `src/ebpf/metrics.c`: eBPF program for collecting various system metrics.
- `src/ebpf/logs.c`: eBPF program for capturing logs and tracing events.
- `src/server/app.py`: Entry point for the Flask server application.
- `src/server/loader.py`: Python script for loading and attaching eBPF programs using `bcc`.
- `src/web/index.html`: Main HTML file for the web dashboard.
- `src/web/dashboard.js`: JavaScript code for fetching and displaying metrics and logs.
- `src/web/styles.css`: CSS styles for the dashboard layout and appearance.
- `Dockerfile.ebpf`: Dockerfile for setting up the eBPF development environment.
- `Dockerfile.web`: Dockerfile for setting up the Flask web server.
- `docker-compose.yml`: Docker Compose file for managing both the eBPF and Flask services.

## Setup Instructions
   - Added instructions for using `docker-compose` to build and run the services.
   - Included steps to verify the compiled `.o` files.

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd ebpf-metrics-dashboard
   ```

2. **Install dependencies:**
   For the web dashboard:
   ```
   cd src/web
   npm install
   ```

3. **Build and run the eBPF programs:**
   Ensure you have the necessary tools installed (e.g., clang, llvm, bpftool) and follow the instructions in the respective eBPF source files.

4. **Run the server:**
   ```
   cd src/server
   python app.py
   ```

5. **Access the dashboard:**
   Open your web browser and navigate to `http://localhost:5000` to view the dashboard.

## Usage Guidelines

- The dashboard will display real-time metrics and logs collected from the system.
- Use the provided API endpoints in `routes.py` to customize or extend functionality.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.