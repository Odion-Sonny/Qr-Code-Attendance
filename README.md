# QR Code Attendance System

The QR Code Attendance System is a user-friendly Python GUI application designed to streamline the process of recording student attendance by generating unique QR codes for each student. With this system, students can effortlessly mark their attendance by simply scanning their individual QR code.

## Requirements

- Python 3.6 or higher

## Setup

1. **Install Python:** Ensure you have Python installed on your system, preferably version 3.6 or higher.

2. **Install Dependencies:** Run the following command to install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```


Usage Steps
Follow these straightforward steps to effectively manage attendance using the QR Code Attendance System:

1. Student Registration
Begin by entering the student IDs into the `students.txt` file. Each student should have a unique ID.

2. QR Code Generation
Execute the following command to generate QR codes for all registered students:

   ```bash
   python generator.py
   ```

This step creates a unique QR code for each student, which will be used for attendance tracking.

3. Distribute QR Codes
Provide each student with their respective QR code, ensuring they receive the correct code based on their ID.

4. Attendance Tracking
To record attendance, run the following command:

   ```bash
   python attend.py
   ```

This application allows you to scan the QR codes presented by students, automatically marking their attendance.


5. Attendance Record
Open the generated `.xlsx` file to access a comprehensive record of student attendance. This Excel file provides an organized overview of attendance data.

By following these steps, you can easily manage student attendance using the QR Code Attendance System, simplifying the process and enhancing accuracy.



