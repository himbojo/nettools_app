# **Net Tools App**

Net Tools App is a web-based utility that provides tools like `ping` and `dig` for network diagnostics. The app features real-time command output streaming and a sleek dark mode UI for a modern user experience.

---

## **Features**
- Perform `ping` and `dig` commands through a web interface.
- Real-time streaming of command output.
- Dark mode UI with a responsive design.
- Dockerized for easy deployment.

---

## **Prerequisites**
Before setting up the application, ensure the following are installed on your system:
- Python 3.10 or higher
- Pip (Python package manager)
- Docker (latest version)

---

## **Environment Setup**
### **1. Local Development (Without Docker)**
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd nettools_app
   ```

2. Create a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python3 run.py
   ```

5. Access the application at:
   ```
   http://localhost:5000
   ```

---

### **2. Dockerized Setup**
Using Docker simplifies deployment and ensures all required tools (`ping`, `dig`) are available in the container.

#### Build the Docker Image:
```bash
docker build -t net-tools-app .
```

#### Run the Docker Container:
```bash
docker run -d -p 5000:5000 --name net-tools-app net-tools-app
```

#### Access the Application:
Open your browser and navigate to:
```
http://localhost:5000
```

#### Stop the Container:
```bash
docker stop net-tools-app
```

#### Remove the Container:
```bash
docker rm net-tools-app
```

---

## **Application Files**
- `run.py`: Entry point for the Flask-SocketIO application.
- `app/`: Contains the Flask app files.
  - `__init__.py`: Initializes the app and Socket.IO.
  - `routes.py`: Defines the backend routes and Socket.IO events.
  - `utils.py`: Contains utility functions for running `ping` and `dig` commands.
- `requirements.txt`: Python dependencies for the application.
- `Dockerfile`: Configuration for building the Docker image.
- `index.html`: Frontend HTML with Bootstrap and custom styling.

---

## **Key Commands**
- **Ping**: Execute `ping` with a hostname and count:
  ```
  ping -c <count> <hostname>
  ```
- **Dig**: Execute `dig` with record types (e.g., A, CNAME, PTR):
  ```
  dig A <hostname>
  dig -x <IP>  # For reverse DNS lookup
  ```

---

## **Technical Notes**
- The application streams output line-by-line from the backend to the frontend using Flask-SocketIO.
- Input is validated to prevent command injection.
- Reverse DNS lookup uses the `-x` flag for the `dig` command.

---

## **Troubleshooting**
### Docker Issues
- **Docker Daemon Not Running**: Start Docker using:
  ```bash
  sudo systemctl start docker
  ```
- **Permission Denied**: Add your user to the Docker group:
  ```bash
  sudo usermod -aG docker $USER
  ```
  Log out and back in for the changes to take effect.

### Application Errors
- **Cannot Access Application**: Ensure the container is running:
  ```bash
  docker ps
  ```

---

## **Future Enhancements**
- Add more networking tools (e.g., traceroute, nslookup).
- Implement user authentication for secure access.
- Support for additional DNS record types.

---

## **License**
This project is licensed under the MIT License. See `LICENSE` for details.