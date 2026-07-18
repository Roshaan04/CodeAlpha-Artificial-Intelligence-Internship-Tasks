#  AI Object Detection and Tracking System

A real-time **AI Object Detection and Tracking System** developed using **Python, OpenCV, and Ultralytics YOLO** as part of the **CodeAlpha Artificial Intelligence Internship**.

The system uses a webcam as a live video source, detects objects in real time using a pretrained YOLO deep learning model, and displays the detected objects with bounding boxes and labels.

The project demonstrates the practical application of **Computer Vision, Deep Learning, Object Detection, and Object Tracking**.

---

## 🚀 Project Overview

Object detection is an important field of Artificial Intelligence and Computer Vision that enables computers to identify and locate objects within images and video.

This project processes live webcam video frames and uses a pretrained **YOLO (You Only Look Once)** model to detect objects.

The general workflow is:

```text
📷 Webcam
    │
    ▼
🎞️ Live Video Frames
    │
    ▼
🖼️ OpenCV Frame Processing
    │
    ▼
🧠 YOLO Object Detection
    │
    ▼
📦 Bounding Boxes
    │
    ▼
🏷️ Object Labels
    │
    ▼
🔢 Object Tracking & IDs
    │
    ▼
🖥️ Real-Time Display
```

The result is a real-time AI vision application capable of detecting and tracking objects through a webcam.

---

# ✨ Features

* 📷 Real-time webcam video input
* 👁️ AI-based object detection
* 🧠 YOLO pretrained deep learning model
* 📦 Bounding boxes around detected objects
* 🏷️ Object class labels
* 🎯 Confidence scores
* 🔢 Object tracking and tracking IDs
* ⚡ Real-time processing
* 🖥️ OpenCV-based video display
* 🔄 Continuous frame-by-frame detection
* 🚪 Easy exit using keyboard controls

---

# 🛠️ Technologies Used

| Technology                 | Purpose                              |
| -------------------------- | ------------------------------------ |
| 🐍 **Python**              | Main programming language            |
| 👁️ **OpenCV**             | Webcam access and video processing   |
| 🧠 **Ultralytics YOLO**    | AI-based object detection            |
| 🔢 **NumPy**               | Numerical and array operations       |
| 🔥 **PyTorch**             | Deep learning framework used by YOLO |
| 🎥 **Computer Vision**     | Real-time visual processing          |
| 📦 **Virtual Environment** | Dependency isolation                 |

---

# 🧠 What is YOLO?

**YOLO** stands for **You Only Look Once**.

It is a real-time object detection algorithm that can identify multiple objects in an image or video frame.

For example, the system may detect:

```text
👤 Person
💻 Laptop
📱 Cell Phone
🪑 Chair
🚗 Car
🐕 Dog
```

Depending on the objects visible in the camera feed.

The YOLO model processes the frame and produces information such as:

* Object class
* Bounding box coordinates
* Confidence score

The application then displays this information on the video.

---

# 🔍 Object Detection vs Object Tracking

## 🎯 Object Detection

Object detection answers:

> "What objects are present in this frame?"

For example:

```text
Person
Laptop
Cell Phone
```

The system draws bounding boxes around detected objects.

---

## 🔢 Object Tracking

Object tracking answers:

> "Which detected object is the same object from the previous frame?"

For example:

```text
Person — ID 1
Person — ID 2
Car — ID 3
```

Tracking IDs help the system maintain the identity of objects across multiple video frames.

This allows the application to follow objects as they move.

---

# ⚙️ How the System Works

The application follows this workflow:

### 1️⃣ Capture Video

OpenCV accesses the computer's webcam.

```text
Webcam → Video Stream
```

---

### 2️⃣ Read Video Frames

The application continuously reads frames from the webcam.

```text
Frame 1
Frame 2
Frame 3
Frame 4
...
```

---

### 3️⃣ Run YOLO Detection

Each frame is passed to the YOLO model.

The model identifies objects within the frame.

---

### 4️⃣ Generate Bounding Boxes

The system draws rectangles around detected objects.

For example:

```text
        ┌──────────────────┐
        │      Person      │
        │                  │
        │        👤        │
        │                  │
        └──────────────────┘
```

---

### 5️⃣ Display Labels

The detected object's name is displayed.

Example:

```text
Person 0.92
```

Where:

```text
Person
```

is the detected class.

And:

```text
0.92
```

represents the model's confidence score.

---

### 6️⃣ Track Objects

The tracking system assigns IDs to objects.

Example:

```text
Person ID: 1
Person ID: 2
```

The ID helps identify the same object across consecutive frames.

---

### 7️⃣ Display the Result

The processed frame is displayed in a live OpenCV window.

The user can observe detection and tracking in real time.

---

# 📂 Project Structure

The project is organized as follows:

```text
Task_4_Object_Detection/
│
├── 📁 src/
│   ├── __init__.py
│   ├── main.py
│   ├── detector.py
│   ├── tracker.py
│   ├── video_processor.py
│   └── config.py
│
├── 📁 output/
│   └── .gitkeep
│
├── 📄 README.md
├── 📄 requirements.txt
└── 📄 .gitignore
```

> The exact source files may vary depending on the final implementation of the project.

---

# 📄 File Descriptions

## `main.py`

The main entry point of the application.

It starts the object detection and tracking system.

Run the application using:

```bash
python src/main.py
```

---

## `detector.py`

Responsible for loading the YOLO model and performing object detection.

The detector identifies objects in each video frame.

---

## `tracker.py`

Responsible for tracking detected objects across consecutive frames and maintaining tracking IDs.

---

## `video_processor.py`

Handles video frame processing and communication between the webcam, detector, and tracking components.

---

## `config.py`

Contains configuration settings such as model paths, confidence thresholds, and other application settings.

---

## `requirements.txt`

Contains the Python packages required to run the project.

---

# ⚙️ Requirements

Before running the project, make sure you have:

* 🐍 Python 3.x
* 📷 A working webcam
* 💻 Windows, macOS, or Linux
* 🌐 Internet connection for downloading the YOLO model on first use

---

# 🚀 Installation

## 1️⃣ Clone the Repository

Clone the CodeAlpha tasks repository:

```bash
git clone https://github.com/YOUR_USERNAME/codealpha_tasks.git
```

Navigate to the Task 4 directory:

```bash
cd codealpha_tasks/Task_4_Object_Detection
```

Replace:

```text
YOUR_USERNAME
```

with your GitHub username.

---

## 2️⃣ Create a Virtual Environment

Create a Python virtual environment:

### Windows

```bash
python -m venv venv
```

### macOS / Linux

```bash
python3 -m venv venv
```

---

## 3️⃣ Activate the Virtual Environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

After activation, your terminal should show:

```text
(venv)
```

---

## 4️⃣ Install Dependencies

Install all required packages using:

```bash
pip install -r requirements.txt
```

The project uses libraries such as:

```text
opencv-python
ultralytics
numpy
torch
torchvision
```

The exact versions are listed in `requirements.txt`.

---

# ▶️ Running the Application

After installing all dependencies, run:

```bash
python src/main.py
```

The application will start the AI Object Detection and Tracking System.

The first time the application runs, the required YOLO model may be downloaded automatically.

---

# 📷 Webcam Usage

Make sure your webcam is connected and available.

When the application starts:

```text
📷 Webcam
    ↓
🎥 Live Video
    ↓
🧠 YOLO Detection
    ↓
📦 Bounding Boxes
    ↓
🔢 Tracking IDs
```

A new window will display the live webcam feed.

Detected objects will appear with bounding boxes and labels.

---

# 🖥️ Expected Output

When the application is running, the webcam window will display a live video feed.

For example:

```text
┌──────────────────────────────────────────────┐
│                                              │
│      ┌───────────────────┐                   │
│      │ Person            │                   │
│      │ Confidence: 0.95  │                   │
│      │ ID: 1             │                   │
│      │                   👤                   │
│      └───────────────────┘                   │
│                                              │
│               AI Object Detection            │
│                  & Tracking                   │
│                                              │
└──────────────────────────────────────────────┘
```

The actual output depends on the objects visible in front of the webcam.

Possible detected objects include:

```text
👤 Person
💻 Laptop
📱 Cell Phone
🪑 Chair
🐕 Dog
🚗 Car
```

---

# 🧪 Testing

The application can be tested using different objects.

### Test 1 — Person Detection

Stand in front of the webcam.

Expected result:

```text
Person detected
Bounding box displayed
Object label displayed
```

---

### Test 2 — Multiple Objects

Place multiple objects in front of the camera.

Expected result:

```text
Object 1 → Detected
Object 2 → Detected
Object 3 → Detected
```

Each detected object should have its own bounding box.

---

### Test 3 — Object Movement

Move around in front of the camera.

Expected result:

```text
Object detected
       ↓
Tracking ID assigned
       ↓
Object moves
       ↓
Tracking ID remains associated
```

This demonstrates the tracking functionality.

---

# 🎮 Controls

The application can be closed using the keyboard control implemented in the program.

Typically:

```text
Q
```

is used to exit the webcam window.

> The exact keyboard control depends on the final implementation of the application.

---

# 🧩 AI Pipeline

The complete AI pipeline is:

```text
📷 Webcam
     │
     ▼
🎞️ Capture Frame
     │
     ▼
🧠 YOLO Object Detection
     │
     ▼
📦 Bounding Box Generation
     │
     ▼
🏷️ Class & Confidence
     │
     ▼
🔢 Object Tracking
     │
     ▼
🆔 Tracking ID
     │
     ▼
🖥️ Display Result
```

---

# 🔐 Virtual Environment

The project uses a Python virtual environment to manage dependencies.

Create it using:

```bash
python -m venv venv
```

Activate it using:

```powershell
.\venv\Scripts\Activate.ps1
```

Deactivate it using:

```bash
deactivate
```

### ⚠️ GitHub Note

The `venv` folder should **not** be uploaded to GitHub.

It is a local environment and can be recreated using the installation commands provided in this README.

---

# 🤖 YOLO Model

This project uses a pretrained YOLO model provided by the Ultralytics framework.

The model is used for real-time object detection.

The model can detect multiple common object classes from the webcam feed.

If the model is not available locally, Ultralytics can download the required model automatically when the application is started.

---

# 🌱 Future Improvements

The project can be extended with:

* 🎥 Video file input
* 📹 IP camera support
* 📊 Object counting
* 🚶 People counting
* 🚗 Vehicle detection
* 📈 FPS monitoring
* 🖥️ Graphical dashboard
* 💾 Save detected video
* 📸 Capture detection screenshots
* 🔊 Audio alerts
* 🚨 Restricted-area alerts
* ☁️ Cloud-based deployment
* 🧠 Custom YOLO model training

---

# 🎯 Learning Objectives

This project demonstrates practical knowledge of:

* Artificial Intelligence
* Computer Vision
* Deep Learning
* Object Detection
* Object Tracking
* YOLO
* OpenCV
* Real-time Video Processing
* Python Programming

---

# 🏆 Internship Task

This project was developed as part of the **CodeAlpha Artificial Intelligence Internship**.

### Completed Task

> **Task 4 — Object Detection and Tracking**

The project demonstrates the implementation of real-time object detection and tracking using a pretrained YOLO model and OpenCV.

---

# 👨‍💻 Author

**Roshan Jadoon**

💻 Interested in Artificial Intelligence, Machine Learning, Computer Vision, Software Development, and Data Structures & Algorithms.

---

# ⭐ Acknowledgements

Special thanks to **CodeAlpha** for providing the opportunity to work on practical Artificial Intelligence projects and gain hands-on experience with real-world AI technologies.

---

## 📜 License

This project was developed for educational and internship purposes as part of the CodeAlpha Artificial Intelligence Internship program.

