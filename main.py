from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import os
import sys
from ttkthemes import ThemedTk

class AttendanceSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Facial Recognition Attendance System")
        self.root.state('zoomed')  # Open in maximized window

        style = ttk.Style(self.root)
        style.theme_use('alt')  # Use a modern theme

        # Centralized Image Paths
        self.image_paths = {
            "toggle": "toggle_button.png",
            "excel": "excel_button.jpg",
            "manual": "stu_details.jpeg"
        }

        # Header Section
        header_frame = Frame(self.root, bg="#2a2a2a", height=100)
        header_frame.pack(fill=X)
        title_lbl = Label(header_frame, text="Facial Recognition Attendance System", font=("Arial", 36, "bold"),
                          fg="white", bg="#2a2a2a")
        title_lbl.pack(pady=20)

        # Main Frame
        main_frame = Frame(self.root, bg="#f5f5f5")
        main_frame.pack(fill=BOTH, expand=True, padx=50, pady=50)

        # Button Section
        btn_frame = Frame(main_frame, bg="#f5f5f5")
        btn_frame.pack(pady=100)

        # Buttons with Images
        self.create_button(btn_frame, self.image_paths["toggle"], "Mark Attendance", self.toggle_backend, 0)
        self.create_button(btn_frame, self.image_paths["excel"], "View Attendance", self.display_excel, 1)
        self.create_button(btn_frame, self.image_paths["manual"], "Add Student", self.manual_attendance, 2)

    def create_button(self, parent, img_path, text, command, col):
        try:
            if os.path.exists(img_path):
                img = Image.open(img_path).resize((150, 150))  # Increased size
                photo_img = ImageTk.PhotoImage(img)
                btn = Button(parent, image=photo_img, command=command, bd=0, bg="#f5f5f5", 
                             activebackground="#e0e0e0", width=160, height=160)
                btn.image = photo_img
                btn.grid(row=0, column=col, padx=40, pady=20)  # Increased spacing

                lbl = Label(parent, text=text, font=("Arial", 16, "bold"), bg="#f5f5f5", fg="#333")
                lbl.grid(row=1, column=col)
            else:
                raise FileNotFoundError(f"Image not found: {img_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def toggle_backend(self):
        try:
            subprocess.Popen([sys.executable, "your_facerecognition_script.py"])  # Ensure correct path
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run backend: {str(e)}")

    def display_excel(self):
        try:
            if os.path.isfile("attendance.xlsx"):
                os.system("start excel attendance.xlsx")
            else:
                raise FileNotFoundError("Attendance Excel file not found!")
        except Exception as e:
            messagebox.showinfo("Error", str(e))

    def manual_attendance(self):
        try:
            subprocess.Popen([sys.executable, "newstd.py"])  # Ensure correct path
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open manual attendance: {str(e)}")

if __name__ == "__main__":
    root = ThemedTk(theme="plastik")  # Use a polished theme
    app = AttendanceSystemGUI(root)
    root.mainloop()
