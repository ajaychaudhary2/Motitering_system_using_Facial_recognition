# 📌 Face Recognition and Identification System 👨‍🦱👨‍🦱

## 📌 Project Overview
The **Attendance System using Facial Recognition** is designed to identify individuals and mark their attendance automatically.

### 🔹 **How it Works**
1. **User Registration**: The user registers in the application by providing necessary details.
2. **Face Capture**: The system captures multiple images of the user and stores them in the database.
3. **Face Recognition**: When the registered user appears in front of the camera again, the system compares the captured image with stored images.
4. **Attendance Marking**: If the user is identified, their attendance is marked.
5. **Report Generation**: Users can generate attendance reports for a specific duration as needed.

---

## 🚀 How to Run the Project

### **Step 1: Create a New Environment**
Open your terminal or **Anaconda Prompt**:

- **Windows**: Search for "Anaconda Prompt" in the Start menu.
- **Ubuntu/Mac**: Open the Terminal.

Run the following command to create a new environment:
```bash
conda create -n facerecognition python==3.6.9
```

### **Step 2: Activate the Environment**
```bash
conda activate facerecognition
```

### **Step 3: Install Dependencies**
Navigate to the project folder:
```bash
cd /path/to/your/project
```
Check if `requirements.txt` exists in the directory:
```bash
# Windows
 dir
# Mac/Linux
 ls
```
If `requirements.txt` is present, install the dependencies:
```bash
pip install -r requirements.txt
```

### **Step 4: Install Additional Dependencies**
Run the following commands:
```bash
conda install anaconda::mxnet
conda install -c conda-forge dlib
pip uninstall numpy
pip uninstall numpy
pip install numpy==1.16.1
```

### **Step 5: Run the Application**
```bash
cd src
python app.py
```

🎉 **You're all set! The application should now be running successfully.** 🎉

---

## 📌 Features
✅ **Face Registration** – Capture and store multiple images of users.  
✅ **Automated Attendance** – Recognizes and marks attendance automatically.  
✅ **Report Generation** – Generate attendance reports based on user requirements.  
✅ **User-friendly Interface** – Easy to use and manage attendance records.  

---

## 📌 Contributing
Feel free to submit issues, pull requests, and suggestions! 🙌

---

## 📌 License
This project is open-source and available under the [MIT License](LICENSE).

