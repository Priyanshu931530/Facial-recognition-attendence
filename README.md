# Facial Recognition Attendance System

A Python-based facial recognition attendance system that uses a webcam to identify registered students and automatically record their attendance.

The project combines **Python, OpenCV, facial recognition, and Excel-based attendance management** to automate the traditional manual attendance process.

---

## 📌 Overview

Managing attendance manually can be time-consuming and prone to errors.

This project provides an automated approach where a webcam captures a student's face, the system detects and recognizes the registered student, and attendance can be recorded with the student's details.

The project was developed as a practical implementation of **Python programming, computer vision, facial recognition, file handling, and automated attendance management**.

---

## ✨ Features

- 📷 Real-time face detection using a webcam
- 👤 Facial recognition of registered students
- 📝 Automated attendance management
- 📊 Attendance data stored in Excel format
- 🕒 Attendance tracking with date/time information
- 🧑‍🎓 Student information management
- 🖥️ Graphical interface for interacting with the application
- 📁 Student image dataset support
- 🔄 Recognition-based attendance workflow
- 🐍 Built using Python

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **OpenCV** | Computer vision and image processing |
| **NumPy** | Numerical and image-data operations |
| **Pandas / Excel tools** | Attendance and data management |
| **Tkinter** | Graphical user interface |
| **OpenPyXL** | Excel file handling |
| **Webcam** | Real-time image capture |

> The exact dependencies used by the project are listed in `requirements.txt`.

---

## 🏗️ Project Structure

```text
Facial-Recognition-Attendance/
│
├── main.py
│       Main application and user interface
│
├── newstd.py
│       Student registration / student management functionality
│
├── your_facerecognition_script.py
│       Facial recognition functionality
│
├── config.py
│       Project configuration
│
├── requirements.txt
│       Python dependencies
│
├── README.md
│       Project documentation
│
├── excel_button.jpg
├── excel_button.png
├── toggle_button.jpg
├── toggle_button.png
├── stu_details.jpeg
│       Interface/supporting image assets
│
├── student_images/
│       Local student face dataset
│       (not included in the public repository)
│
└── attendance.xlsx
        Local attendance records
        (not included in the public repository)
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Priyanshu931530/facial-recognition-attendance.git
```

Move into the project directory:

```bash
cd facial-recognition-attendance
```

---

## 2. Create a Virtual Environment

On Windows:

```bash
python -m venv .venv
```

Activate the virtual environment using Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

If activation is successful, you should see:

```text
(.venv)
```

before your terminal path.

---

## 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

After activating the virtual environment and installing the dependencies, run the main application:

```bash
python main.py
```

Make sure a working webcam is connected to your computer.

---

# 👤 Student Registration

Before facial recognition can identify a student, the student's information and facial data need to be registered.

The general workflow is:

```text
Student Information
        ↓
Face/Image Capture
        ↓
Student Image Dataset
        ↓
Facial Recognition
        ↓
Student Identification
        ↓
Attendance Recording
```

The student images are maintained locally and are intentionally excluded from the public GitHub repository.

---

# 📷 Facial Recognition Workflow

The facial recognition process follows these general steps:

### 1. Webcam Input

The webcam captures frames continuously.

### 2. Face Detection

The system processes the captured frames and detects faces.

### 3. Face Recognition

The detected face is compared against the registered student facial data.

### 4. Student Identification

When a registered face is recognized, the corresponding student information can be retrieved.

### 5. Attendance

The recognized student's attendance is recorded in the attendance system.

---

# 📊 Attendance Management

The project uses an Excel-based approach for storing attendance information.

Attendance data may include information such as:

```text
Student Name
Student ID
Date
Time
Attendance Status
```

The actual attendance file is maintained locally and is **not included in the public GitHub repository**.

---

# 🔐 Data Privacy

This project works with facial images and attendance information, which may contain sensitive personal data.

For this reason, the following files are excluded from the public repository:

```text
student_images/
attendance.xlsx
```

The `.gitignore` file prevents these files from being accidentally committed.

### Important

Do not upload real student facial images, attendance records, passwords, API keys, or other sensitive information to a public repository.

If the project is deployed in a real environment, appropriate consent, security controls, and data-retention policies should be considered.

---

# 📁 GitHub Repository Structure

The public repository intentionally contains the application source code and supporting assets but does not contain personal biometric data.

```text
📦 facial-recognition-attendance
│
├── 🐍 main.py
├── 🐍 newstd.py
├── 🐍 your_facerecognition_script.py
├── ⚙️ config.py
├── 📦 requirements.txt
├── 📖 README.md
│
└── 🖼️ Supporting UI assets
```

---

# ⚠️ Limitations

Like most computer-vision-based facial recognition systems, performance can be affected by:

- Poor lighting
- Camera quality
- Face angle
- Significant changes in appearance
- Occlusion such as masks or sunglasses
- Similar-looking faces
- Quality and size of the registered dataset
- Hardware performance

The system should therefore be considered an **attendance automation project**, not a high-security biometric identification system.

---

# 🚀 Future Improvements

The project can be further improved by adding:

- Anti-spoofing / liveness detection
- Improved recognition accuracy
- Database integration
- Web-based attendance dashboard
- Admin authentication
- Student management dashboard
- Attendance report generation
- Search and filtering of attendance records
- Cloud-based data storage
- Email notifications
- Multi-camera support
- Better handling of low-light environments
- Secure encrypted storage of biometric information

---

# 🎯 Learning Outcomes

This project provided practical experience with:

- Python programming
- OpenCV
- Computer vision
- Facial recognition
- Image processing
- Webcam integration
- GUI development
- Excel file handling
- File management
- Real-time application development
- Python package management
- Git and GitHub

---

# 💡 Why This Project?

The main purpose of this project is to demonstrate how computer vision can be applied to automate a real-world administrative task.

Instead of relying completely on manual attendance marking, the system provides an automated workflow based on facial recognition.

---

# 🔮 Future Scope

The project can be developed into a complete attendance management platform with:

```text
Facial Recognition
        ↓
Backend Database
        ↓
Attendance Management
        ↓
Web Dashboard
        ↓
Reports & Analytics
```

Such an architecture could allow administrators to manage students, monitor attendance, generate reports, and manage recognition data from a centralized system.

---

# 👨‍💻 Author

**Priyanshu Jangid**

B.Tech — Computer Science & Engineering  
Raj Kumar Goel Institute of Technology (RKGIT)

GitHub: [@Priyanshu931530](https://github.com/Priyanshu931530)

---

# 📄 License

This project is intended primarily for educational and demonstration purposes.

If you plan to use the project in a real-world environment, review the applicable privacy, biometric-data, and data-protection requirements before deployment.

---

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub.
