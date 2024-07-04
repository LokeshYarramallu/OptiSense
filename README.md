# OptiSense

## AC Control System with Real-Time Monitoring

This project is a comprehensive system designed to control an air conditioning (AC) unit based on real-time monitoring of people count. It integrates multiple components including a server, client applications, and cloud-based data storage to ensure efficient and automated AC management.

### Key Features

1. **Server-Client Architecture**:
   - **Server**: Manages connections from multiple clients, processes requests, and communicates with cloud storage.
   - **Clients**: Two client applications – one for AC control (Tkinter-based) and another for real-time data visualization (Flask-based web interface).

2. **Real-Time People Counting**:
   - Uses a YOLO object detection model to count people in a given area via a camera feed.
   - Adjusts AC settings dynamically based on the number of people detected.

3. **AC Control**:
   - A Tkinter-based GUI for real-time AC control.
   - Dynamically updates temperature and fan speed based on the number of people detected.

4. **Cloud Integration**:
   - Firebase is used to store and retrieve data, ensuring persistent and accessible records of AC status and people count.

5. **Web Interface**:
   - A Flask-based web application provides a user-friendly interface to visualize real-time AC status and historical data.
   - Uses Bootstrap for a responsive and modern design.

### Components

- **Server**:
  - Handles client connections, processes requests, and manages data transfer between clients and Firebase.
  
- **AC Client**:
  - Tkinter-based application for controlling the AC unit. Adjusts temperature and fan speed based on real-time people count.

- **Web Client**:
  - Flask application that fetches and displays data from the server. Uses AJAX for real-time updates.

- **People Counting Module**:
  - Utilizes YOLO for object detection to count the number of people in the camera's view.

- **Firebase Integration**:
  - Stores AC status and people count data. Provides methods for pushing and retrieving data.

### Setup and Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/LokeshYarramallu/OptiSense.git
   cd ac-control-system
   ```

2. **Install dependencies**:
   - Python libraries:
     ```sh
     pip install -r requirements.txt
     ```
   - Ensure you have OpenCV and the YOLO model installed and configured.

3. **Configure Firebase**:
   - Add your Firebase credentials JSON file to the project directory.

4. **Run the server**:
   ```sh
   python server.py
   ```

5. **Run the AC client**:
   ```sh
   python ac_client.py
   ```

6. **Run the web client**:
   ```sh
   python ui_client.py
   ```

### Usage

- **AC Control**:
  - The Tkinter GUI will launch, showing the current status of the AC unit.
  - The system will automatically adjust the AC settings based on the real-time people count.

- **Web Interface**:
  - Access the Flask web application through your browser to visualize real-time AC status and historical data.

### Future Improvements

- Enhance error handling and logging for better maintenance and debugging.
- Implement more advanced AC control algorithms for optimized energy usage.
- Add user authentication for secure access to the web interface.

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

### License

This project is licensed under the MIT License.

---

Feel free to adjust this description to better fit your project's specific details and goals.
