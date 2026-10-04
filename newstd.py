import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import mysql.connector
import shutil
import os
from datetime import datetime
from tkcalendar import DateEntry


class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1024x768")
        self.root.config(bg="#f0f0f0")  # Light gray background

        # Apply modern style
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Modern theme
        self.style.configure('TLabel', background="#f0f0f0", font=('Helvetica', 10))
        self.style.configure('TEntry', padding=5)
        self.style.configure('TButton', padding=10, font=('Helvetica', 10))
        self.style.configure('Treeview', rowheight=25, font=('Helvetica', 9))
        self.style.configure('TLabelframe', background="#f0f0f0")

        # Database connection
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="student_management"
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error connecting to database: {err}")
            self.root.quit()

        # Variables
        self.name_var = tk.StringVar()
        self.roll_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.dob_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.address_var = tk.StringVar()
        self.image_path = ""

        # Create modern UI
        self.create_modern_widgets()

    def create_modern_widgets(self):
        # Main title with modern styling
        title_frame = ttk.Frame(self.root, style='TFrame')
        title_frame.pack(fill='x', padx=20, pady=20)

        title_label = ttk.Label(title_frame, text="Student Management System", font=('Helvetica', 24, 'bold'))
        title_label.pack()

        # Create main container
        main_container = ttk.Frame(self.root)
        main_container.pack(fill='both', expand=True, padx=20, pady=10)

        # Left panel for input
        input_frame = ttk.LabelFrame(main_container, text="Student Details", padding=15)
        input_frame.pack(side='left', fill='y', padx=(0, 10))

        # Modern input fields
        input_fields = [
            ("Name", self.name_var),
            ("Roll Number", self.roll_var),
            ("Email", self.email_var),
            ("Phone", self.phone_var),
            ("Address", self.address_var)
        ]

        for i, (label, var) in enumerate(input_fields):
            ttk.Label(input_frame, text=label).grid(row=i, column=0, padx=5, pady=8, sticky='w')
            ttk.Entry(input_frame, textvariable=var, width=30).grid(row=i, column=1, padx=5, pady=8)

        # Gender dropdown with modern styling
        ttk.Label(input_frame, text="Gender").grid(row=len(input_fields), column=0, padx=5, pady=8, sticky='w')
        gender_combo = ttk.Combobox(input_frame, textvariable=self.gender_var,
                                    values=["Male", "Female", "Other"], width=27)
        gender_combo.grid(row=len(input_fields), column=1, padx=5, pady=8)

        # Date of Birth field
        ttk.Label(input_frame, text="Date of Birth").grid(row=len(input_fields) + 1, column=0, padx=5, pady=8,
                                                          sticky='w')

        # Use the DateEntry widget from tkcalendar to ensure correct date format
        self.dob_entry = DateEntry(input_frame, textvariable=self.dob_var, width=30, date_pattern='dd/mm/yyyy')
        self.dob_entry.grid(row=len(input_fields) + 1, column=1, padx=5, pady=8)

        # Image upload button
        upload_btn = ttk.Button(input_frame, text="Upload Image", command=self.upload_image, style='TButton')
        upload_btn.grid(row=len(input_fields) + 2, column=0, columnspan=2, pady=15)

        # Action buttons frame
        btn_frame = ttk.Frame(input_frame)
        btn_frame.grid(row=len(input_fields) + 3, column=0, columnspan=2, pady=15)

        # Modern styled buttons
        buttons = [
            ("Add Student", self.add_student, '#28a745'),
            ("Update", self.update_student, '#007bff'),
            ("Delete", self.delete_student, '#dc3545'),
            ("Clear", self.clear_fields, '#6c757d')
        ]

        for i, (text, command, color) in enumerate(buttons):
            btn = ttk.Button(btn_frame, text=text, command=command, style='TButton')
            btn.pack(side='left', padx=5)

        # Right panel with Treeview
        tree_frame = ttk.Frame(main_container)
        tree_frame.pack(side='right', fill='both', expand=True)

        # Modern Treeview
        self.tree = ttk.Treeview(tree_frame,
                                 columns=("ID", "Name", "Roll", "Gender", "DOB", "Email", "Phone", "Address"),
                                 show="headings", style='Custom.Treeview')

        # Configure columns
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col, anchor='center')
            self.tree.column(col, anchor='center', width=100)

        # Add scrollbars
        y_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        x_scroll = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

        # Pack scrollbars and treeview
        y_scroll.pack(side="right", fill="y")
        x_scroll.pack(side="bottom", fill="x")
        self.tree.pack(fill="both", expand=True)

        # Load initial data
        self.load_students()

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")])
        if file_path:
            # Create images directory if it doesn't exist
            if not os.path.exists("student_images"):
                os.makedirs("student_images")

            # Copy image to student_images directory
            new_path = f"student_images/{datetime.now().strftime('%Y%m%d%H%M%S')}_{os.path.basename(file_path)}"
            shutil.copy2(file_path, new_path)
            self.image_path = new_path

    def add_student(self):
        if not all([self.name_var.get(), self.roll_var.get()]):
            messagebox.showerror("Error", "Name and Roll Number are required!")
            return

        # Validate and format the Date of Birth
        dob = self.dob_var.get()
        try:
            # Try to parse the date in the format 'DD/MM/YYYY'
            formatted_dob = datetime.strptime(dob, "%d/%m/%Y").date()
        except ValueError:
            # If the date format is incorrect, show an error message
            messagebox.showerror("Error", "Please enter a valid Date of Birth in DD/MM/YYYY format.")
            return

        # Now proceed with adding the student
        try:
            sql = """INSERT INTO student_details 
                    (name, roll_number, gender, date_of_birth, email, phone, address, image_path) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (
                self.name_var.get(),
                self.roll_var.get(),
                self.gender_var.get(),
                formatted_dob,
                self.email_var.get(),
                self.phone_var.get(),
                self.address_var.get(),
                self.image_path
            )
            self.cursor.execute(sql, values)
            self.conn.commit()
            messagebox.showinfo("Success", "Student added successfully!")
            self.clear_fields()
            self.load_students()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")

    def update_student(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a student to update!")
            return

        # Validate and format the Date of Birth
        dob = self.dob_var.get()
        try:
            # Try to parse the date in the format 'DD/MM/YYYY'
            formatted_dob = datetime.strptime(dob, "%d/%m/%Y").date()
        except ValueError:
            # If the date format is incorrect, show an error message
            messagebox.showerror("Error", "Please enter a valid Date of Birth in DD/MM/YYYY format.")
            return

        try:
            student_id = self.tree.item(selected[0])["values"][0]
            sql = """UPDATE student_details 
                    SET name=%s, roll_number=%s, gender=%s, date_of_birth=%s, 
                    email=%s, phone=%s, address=%s, image_path=%s 
                    WHERE id=%s"""
            values = (
                self.name_var.get(),
                self.roll_var.get(),
                self.gender_var.get(),
                formatted_dob,
                self.email_var.get(),
                self.phone_var.get(),
                self.address_var.get(),
                self.image_path,
                student_id
            )
            self.cursor.execute(sql, values)
            self.conn.commit()
            messagebox.showinfo("Success", "Student updated successfully!")
            self.clear_fields()
            self.load_students()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")

    def delete_student(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a student to delete!")
            return

        if messagebox.askyesno("Confirm", "Are you sure you want to delete this student?"):
            try:
                student_id = self.tree.item(selected[0])["values"][0]
                self.cursor.execute("DELETE FROM student_details WHERE id=%s", (student_id,))
                self.conn.commit()
                messagebox.showinfo("Success", "Student deleted successfully!")
                self.clear_fields()
                self.load_students()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database error: {err}")

    def clear_fields(self):
        self.name_var.set("")
        self.roll_var.set("")
        self.gender_var.set("")
        self.dob_var.set("")
        self.email_var.set("")
        self.phone_var.set("")
        self.address_var.set("")
        self.image_path = ""

    def load_students(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Load students from database
        try:
            self.cursor.execute("SELECT * FROM student_details")
            students = self.cursor.fetchall()
            for student in students:
                self.tree.insert("", "end", values=student)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")

    def __del__(self):
        if hasattr(self, 'conn') and self.conn.is_connected():
            self.cursor.close()
            self.conn.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
