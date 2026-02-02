# Color Detection — Quick Start

## Important notes

- **OS:** These instructions assume **Windows** (PowerShell). If you use WSL2 or a Linux host, a few Docker/device steps differ.
- **Python & venv:** Use a virtual environment to avoid global package conflicts.
- **OpenCV in Docker:** Use **opencv-python-headless** in containers (no GUI). On your Windows host, use **opencv-python** if you need GUI windows.
- **OneDrive:** Project folders on OneDrive may cause file-locking or performance issues — consider moving the project outside OneDrive for development.
- **Camera access:** Passing a physical camera into a container on Windows is non-trivial. For Docker, prefer using a sample video file or run the app locally when using a webcam.

---

## Installation (Windows / PowerShell)

1. Install Python 3.8+ (recommended 3.11+):

   - Download from https://python.org and ensure "Add Python to PATH" is checked.

2. Create and activate a virtual environment:

   ```powershell
   cd "C:\Users\<you>\path\to\project"
   python -m venv venv
   # PowerShell activation
   .\venv\Scripts\Activate.ps1
   # If activation is blocked, you may need:
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

3. Install dependencies:

   - If you have a `requirements.txt` file:
     ```powershell
     pip install -r requirements.txt
     ```
   - Otherwise, install OpenCV and any extras directly:
     ```powershell
     pip install opencv-python
     # add other packages as needed, e.g. numpy
     pip install numpy
     ```

4. Run the app:

   ```powershell
   python main.py
   ```

---

## Docker: Build container from scratch (Windows)

### Sample Dockerfile (recommended)

```dockerfile
# Use a small Python base
FROM python:3.11-slim

WORKDIR /app

# Install system deps if needed (uncomment if required for OpenCV binary wheels)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential ffmpeg libsm6 libxext6 && rm -rf /var/lib/apt/lists/*

# Copy requirements and install (use opencv-python-headless in container unless GUI needed)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Default command
CMD ["python", "main.py"]
```

- Put your dependencies in `requirements.txt`, for example:
  ```text
  opencv-python-headless
  numpy
  ```

### Build the Docker image (PowerShell)

```powershell
# From project root (where Dockerfile is)
docker build -t color-detection:latest .
```

### Run the Docker container (PowerShell)

- Run interactively:

```powershell
docker run --rm -it --name color-detection color-detection:latest
```

- If your app exposes a port (example 5000):

```powershell
docker run --rm -it -p 5000:5000 --name color-detection color-detection:latest
```

- Mount the project directory into the container (for live-editing):

```powershell
# On Docker Desktop with WSL2 this works: -v ${PWD}:/app
docker run --rm -it -v ${PWD}:/app -w /app color-detection:latest
```

> ⚠️ Note: On Windows, mounting and device passthrough may require Docker Desktop with WSL2 backend. Camera devices typically require Linux device paths (e.g., `/dev/video0`) and are not straightforward on native Windows Docker.

---

## 🛠 Troubleshooting & Tips

- If OpenCV GUI windows fail inside Docker, use `opencv-python-headless` to avoid X-server issues and run GUI locally.
- If `pip install opencv-python` fails on Windows, install the latest Visual C++ Redistributable from Microsoft.
- For camera testing, prefer running `python main.py` locally; use Docker for processing files or server-style deployments.

---

If you'd like, I can also:
- Add a `requirements.txt` file and a minimal `Dockerfile` into the repo ✅
- Add a short sample command in `main.py` to serve results over HTTP for easier container usage ✅

