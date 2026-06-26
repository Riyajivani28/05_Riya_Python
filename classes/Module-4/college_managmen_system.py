import os
import sqlite3
import re
import time 
from tkinter import *
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk, ImageOps

class CollegeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("College Management System")
        self.root.geometry("1350x720+10+10")
        
        # --- Light Pink Theme Colors ---
        self.bg_color = "#FFF0F5"       # Lavender Blush
        self.frame_color = "#FFFFFF"    # White
        self.btn_color = "#FFB6C1"      # Light Pink
        self.header_color = "#FF69B4"   # Hot Pink
        
        self.root.config(bg=self.bg_color)

        # --- DATABASE SETUP ---
        self.conn = sqlite3.connect("college_data.db")
        self.cursor = self.conn.cursor()
        self.create_table()

        # --- VARIABLES ---
        self.var_id = StringVar()
        self.var_photo = StringVar()
        self.var_enrollment = StringVar()
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_mobile = StringVar()
        self.var_address = StringVar()
        self.var_course = StringVar()
        self.var_semester = StringVar()
        self.var_attendance = StringVar()
        self.var_fees_paid = StringVar()
        self.var_fees_pending = StringVar()
        self.var_marks = StringVar()
        self.var_grade = StringVar()
        
        self.search_by = StringVar()
        self.search_txt = StringVar()

        # --- HEADER TITLE ---
        title = Label(self.root, text="COLLEGE MANAGEMENT SYSTEM", font=("times new roman", 30, "bold"), 
                      bg=self.header_color, fg="white", bd=5, relief=GROOVE)
        title.pack(side=TOP, fill=X)

        # --- MANAGE FRAME (LEFT) ---
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg=self.frame_color)
        Manage_Frame.place(x=20, y=80, width=470, height=620)

        m_title = Label(Manage_Frame, text="Student Details Form", font=("times new roman", 18, "bold"), 
                        bg=self.frame_color, fg=self.header_color)
        m_title.grid(row=0, columnspan=3, pady=10)

        # --- FORM FIELDS ---
        labels = [
            ("Enrollment", self.var_enrollment, 1),
            ("Name", self.var_name, 2),
            ("DOB", self.var_dob, 3),
            ("Email", self.var_email, 4),
            ("Mobile", self.var_mobile, 5),
            ("Address", self.var_address, 6),
            ("Course", self.var_course, 7),
            ("Attendance (%)", self.var_attendance, 10),
            ("Fees Paid", self.var_fees_paid, 11),
            ("Fees Pending", self.var_fees_pending, 12),
            ("Marks", self.var_marks, 13),
            ("Grade", self.var_grade, 14)
        ]

        for text, var, row in labels:
            lbl = Label(Manage_Frame, text=text, font=("arial", 11, "bold"), bg=self.frame_color)
            lbl.grid(row=row, column=0, pady=5, padx=10, sticky="w")
            ent = Entry(Manage_Frame, textvariable=var, font=("arial", 11), bd=2, relief=GROOVE, width=20)
            ent.grid(row=row, column=1, pady=5, padx=5, sticky="w")

        # Gender Dropdown
        lbl_gender = Label(Manage_Frame, text="Gender", font=("arial", 11, "bold"), bg=self.frame_color)
        lbl_gender.grid(row=8, column=0, pady=5, padx=10, sticky="w")
        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.var_gender, font=("arial", 10), state="readonly", width=18)
        combo_gender['values'] = ("Male", "Female", "Other")
        combo_gender.grid(row=8, column=1, pady=5, padx=5, sticky="w")

        # Semester Dropdown
        lbl_sem = Label(Manage_Frame, text="Semester", font=("arial", 11, "bold"), bg=self.frame_color)
        lbl_sem.grid(row=9, column=0, pady=5, padx=10, sticky="w")
        combo_sem = ttk.Combobox(Manage_Frame, textvariable=self.var_semester, font=("arial", 10), state="readonly", width=18)
        combo_sem['values'] = ("Sem 1", "Sem 2", "Sem 3", "Sem 4", "Sem 5", "Sem 6", "Sem 7", "Sem 8")
        combo_sem.grid(row=9, column=1, pady=5, padx=5, sticky="w")

        # --- PHOTO SECTION ---
        self.lbl_photo = Label(Manage_Frame, text="No Image", bg="#eee", bd=2, relief=RIDGE, font=("arial", 10))
        self.lbl_photo.place(x=325, y=60, width=120, height=130)
        
        btn_upload = Button(Manage_Frame, text="Upload Photo", command=self.upload_photo, bg=self.btn_color, font=("arial", 10, "bold"), cursor="hand2")
        btn_upload.place(x=325, y=200, width=120, height=30)

        # --- BUTTONS ---
        btn_F = Frame(Manage_Frame, bg=self.frame_color)
        btn_F.place(x=5, y=560, width=455)
        
        Button(btn_F, text="Add", command=self.add_student, font=("arial", 11, "bold"), width=8, bg="lightgreen", cursor="hand2").grid(row=0, column=0, padx=5)
        Button(btn_F, text="Update", command=self.update_student, font=("arial", 11, "bold"), width=8, bg="lightblue", cursor="hand2").grid(row=0, column=1, padx=5)
        Button(btn_F, text="Delete", command=self.delete_student, font=("arial", 11, "bold"), width=8, bg="#FF7276", cursor="hand2").grid(row=0, column=2, padx=5)
        Button(btn_F, text="Clear", command=self.clear_fields, font=("arial", 11, "bold"), width=8, bg="yellow", cursor="hand2").grid(row=0, column=3, padx=5)
        Button(btn_F, text="Receipt", command=self.generate_receipt, font=("arial", 11, "bold"), width=8, bg="orange", cursor="hand2").grid(row=0, column=4, padx=5)

        # --- DETAILS FRAME (RIGHT) ---
        Details_Frame = Frame(self.root, bd=4, relief=RIDGE, bg=self.frame_color)
        Details_Frame.place(x=510, y=80, width=820, height=620)

        lbl_search = Label(Details_Frame, text="Search By", font=("arial", 12, "bold"), bg=self.frame_color)
        lbl_search.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        combo_search = ttk.Combobox(Details_Frame, textvariable=self.search_by, width=12, font=("arial", 11), state="readonly")
        combo_search['values'] = ("Enrollment", "Name", "Mobile")
        combo_search.grid(row=0, column=1, padx=10, pady=10)
        combo_search.current(0)

        txt_search = Entry(Details_Frame, textvariable=self.search_txt, font=("arial", 11), bd=2, relief=GROOVE, width=20)
        txt_search.grid(row=0, column=2, padx=10, pady=10)

        Button(Details_Frame, text="Search", command=self.search_data, font=("arial", 10, "bold"), width=10, bg=self.btn_color, cursor="hand2").grid(row=0, column=3, padx=10)
        Button(Details_Frame, text="Show All", command=self.fetch_data, font=("arial", 10, "bold"), width=10, bg=self.btn_color, cursor="hand2").grid(row=0, column=4, padx=10)

        # --- TABLE VIEW (TREEVIEW) ---
        Table_Frame = Frame(Details_Frame, bd=2, relief=RIDGE, bg="white")
        Table_Frame.place(x=10, y=60, width=790, height=540)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        
        self.Student_Table = ttk.Treeview(Table_Frame, columns=("id", "photo", "enrollment", "name", "gender", "dob", "email", "mobile", "address", "course", "semester", "attendance", "fees_paid", "fees_pending", "marks", "grade"), 
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.config(command=self.Student_Table.xview)
        scroll_y.config(command=self.Student_Table.yview)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        headings = [
            ("id", "ID"), ("enrollment", "Enrollment"), ("name", "Name"), 
            ("gender", "Gender"), ("dob", "DOB"), ("email", "Email"), ("mobile", "Mobile"), 
            ("address", "Address"), ("course", "Course"), ("semester", "Semester"), 
            ("attendance", "Attend %"), ("fees_paid", "Paid"), ("fees_pending", "Pending"), 
            ("marks", "Marks"), ("grade", "Grade")
        ]
        
        for col_name, text in headings:
            self.Student_Table.heading(col_name, text=text)
            if col_name == "id":
                self.Student_Table.column(col_name, width=40, anchor="center")
            else:
                self.Student_Table.column(col_name, width=105)

        self.Student_Table.heading("photo", text="")
        self.Student_Table.column("photo", width=0, stretch=NO)

        self.Student_Table["show"] = "headings"
        self.Student_Table.pack(fill=BOTH, expand=1)
        self.Student_Table.bind("<ButtonRelease-1>", self.get_cursor)
        
        self.fetch_data()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT, photo TEXT, enrollment TEXT UNIQUE, name TEXT, gender TEXT, 
            dob TEXT, email TEXT, mobile TEXT, address TEXT, course TEXT, semester TEXT, 
            attendance TEXT, fees_paid REAL, fees_pending REAL, marks REAL, grade TEXT)""")
        self.conn.commit()

    def upload_photo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.var_photo.set(file_path)
            self.display_image(file_path)

    def display_image(self, path):
        try:
            path = str(path).strip()
            if path and os.path.exists(path):
                img = Image.open(path)
                img = ImageOps.exif_transpose(img)
                img = img.resize((120, 130), Image.Resampling.LANCZOS)
                self.img_tk = ImageTk.PhotoImage(img)
                self.lbl_photo.config(image=self.img_tk, text="")
                self.lbl_photo.image = self.img_tk
            else:
                self.lbl_photo.config(image="", text="No Image")
        except Exception:
            self.lbl_photo.config(image="", text="No Image")

    # --- IMAGE REMOVED FROM GENERATE RECEIPT ---
    def generate_receipt(self):
        if self.var_enrollment.get().strip() == "" or self.var_name.get().strip() == "":
            messagebox.showerror("Error", "Please select a student record from the table first to generate a receipt!")
            return

        enrollment_id = self.var_enrollment.get().strip()
        pdf_name = f"Receipts/Receipt_{enrollment_id}.pdf"

        try:
            from reportlab.pdfgen import canvas
            from reportlab.lib.pagesizes import letter
            
            if not os.path.exists("Receipts"):
                os.makedirs("Receipts")

            if os.path.exists(pdf_name):
                try:
                    os.rename(pdf_name, pdf_name)
                except OSError:
                    messagebox.showerror("Permission Denied", f"Receipt_{enrollment_id}.pdf background ma open che. Pehla ene close karo.")
                    return

            c = canvas.Canvas(pdf_name, pagesize=letter)
            
            # Layout Borders
            c.setFillColor("#FF69B4") 
            c.rect(20, 20, 572, 752, stroke=1, fill=0) 
            c.rect(30, 700, 552, 50, stroke=0, fill=1) 
            
            # Title
            c.setFillColor("white")
            c.setFont("Helvetica-Bold", 20)
            c.drawCentredString(306, 715, "COLLEGE FEES RECEIPT")
            
            # --- IMAGE AND PLACEHOLDER BOX ARE REMOVED ENTIRELY ---

            c.setFillColor("black")
            y_position = 640
            line_height = 30
            
            invoice_data = [
                ("Enrollment No:", self.var_enrollment.get()),
                ("Student Name:", self.var_name.get()),
                ("Course Program:", self.var_course.get()),
                ("Current Semester:", self.var_semester.get()),
                ("Registered Email:", self.var_email.get()),
                ("Contact Number:", self.var_mobile.get()),
            ]
            
            for label, value in invoice_data:
                c.setFont("Helvetica-Bold", 12)
                c.drawString(60, y_position, label)
                c.setFont("Helvetica", 12)
                c.drawString(200, y_position, str(value))
                y_position -= line_height
                
            c.setStrokeColor("#FFB6C1")
            c.setLineWidth(1.5)
            c.line(50, y_position, 550, y_position)
            y_position -= 40
            
            c.setFont("Helvetica-Bold", 13)
            c.setFillColor("#FF69B4")
            c.drawString(60, y_position, "FINANCIAL ACCOUNT SUMMARY")
            c.setFillColor("black")
            y_position -= 30
            
            c.setFont("Helvetica-Bold", 12)
            c.drawString(60, y_position, "Fees Paid Status:")
            c.setFont("Helvetica", 12)
            c.drawString(200, y_position, f"INR {self.var_fees_paid.get()} /-")
            y_position -= line_height
            
            c.setFont("Helvetica-Bold", 12)
            c.drawString(60, y_position, "Fees Outstanding:")
            c.setFont("Helvetica", 12)
            c.drawString(200, y_position, f"INR {self.var_fees_pending.get()} /-")
            
            c.setFont("Helvetica-Oblique", 10)
            c.drawRightString(540, 50, "Authorized College Management Signature")
            
            c.showPage()  
            c.save()
            
            del c
            time.sleep(0.5)

            full_path = os.path.abspath(pdf_name)
            if os.path.exists(full_path):
                os.startfile(full_path)

        except Exception as e:
            messagebox.showerror("Error", f"Could not generate or open PDF file.\nDetails: {str(e)}")

    def validate_inputs(self):
        if (self.var_enrollment.get().strip() == "" or self.var_name.get().strip() == "" or 
            self.var_dob.get().strip() == "" or self.var_email.get().strip() == "" or 
            self.var_mobile.get().strip() == "" or self.var_address.get().strip() == "" or 
            self.var_course.get().strip() == "" or self.var_gender.get().strip() == "" or 
            self.var_semester.get().strip() == "" or self.var_attendance.get().strip() == "" or 
            self.var_fees_paid.get().strip() == "" or self.var_fees_pending.get().strip() == "" or 
            self.var_marks.get().strip() == "" or self.var_grade.get().strip() == ""):
            
            messagebox.showerror("Error", "All fields are mandatory!")
            return False

        if self.var_photo.get().strip() == "":
            messagebox.showerror("Error", "Please upload a student photo!")
            return False

        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, self.var_email.get().strip()):
            messagebox.showerror("Error", "Invalid Email Format! (e.g., example@domain.com)")
            return False
        
        mobile_pattern = r'^\d{10}$'
        if not re.match(mobile_pattern, self.var_mobile.get().strip()):
            messagebox.showerror("Error", "Mobile number must be exactly 10 digits!")
            return False
            
        return True

    def add_student(self):
        if not self.validate_inputs():
            return
        try:
            self.cursor.execute("""INSERT INTO students (photo, enrollment, name, gender, dob, email, mobile, address, course, semester, attendance, fees_paid, fees_pending, marks, grade) 
                                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", 
                               (self.var_photo.get(), self.var_enrollment.get(), self.var_name.get(), self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_mobile.get(), self.var_address.get(), self.var_course.get(), self.var_semester.get(), self.var_attendance.get(), self.var_fees_paid.get(), self.var_fees_pending.get(), self.var_marks.get(), self.var_grade.get()))
            self.conn.commit()
            self.fetch_data()
            self.clear_fields()
            messagebox.showinfo("Success", "Student Added Successfully")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Enrollment Number already exists!")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

    def fetch_data(self):
        self.cursor.execute("SELECT * FROM students")
        rows = self.cursor.fetchall()
        self.Student_Table.delete(*self.Student_Table.get_children())
        for row in rows:
            self.Student_Table.insert('', END, values=row)

    def clear_fields(self):
        self.var_id.set("")
        self.var_photo.set("")
        self.var_enrollment.set("")
        self.var_name.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_mobile.set("")
        self.var_address.set("")
        self.var_course.set("")
        self.var_semester.set("")
        self.var_attendance.set("")
        self.var_fees_paid.set("")
        self.var_fees_pending.set("")
        self.var_marks.set("")
        self.var_grade.set("")
        self.lbl_photo.config(image="", text="No Image")

    def get_cursor(self, ev):
        try:
            cursor_row = self.Student_Table.focus()
            content = self.Student_Table.item(cursor_row)
            row = content['values']
            if row:
                self.var_id.set(row[0])
                self.var_photo.set(row[1]) 
                self.var_enrollment.set(row[2])
                self.var_name.set(row[3])
                self.var_gender.set(row[4])
                self.var_dob.set(row[5])
                self.var_email.set(row[6])
                self.var_mobile.set(row[7])
                self.var_address.set(row[8])
                self.var_course.set(row[9])
                self.var_semester.set(row[10])
                self.var_attendance.set(row[11])
                self.var_fees_paid.set(row[12])
                self.var_fees_pending.set(row[13])
                self.var_marks.set(row[14])
                self.var_grade.set(row[15])
                
                self.display_image(row[1])
        except Exception:
            pass

    def update_student(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Please select a student record to update.")
            return
        if not self.validate_inputs():
            return
        try:
            self.cursor.execute("""UPDATE students SET photo=?, enrollment=?, name=?, gender=?, dob=?, email=?, mobile=?, address=?, course=?, semester=?, attendance=?, fees_paid=?, fees_pending=?, marks=?, grade=? WHERE id=?""", 
                               (self.var_photo.get(), self.var_enrollment.get(), self.var_name.get(), self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_mobile.get(), self.var_address.get(), self.var_course.get(), self.var_semester.get(), self.var_attendance.get(), self.var_fees_paid.get(), self.var_fees_pending.get(), self.var_marks.get(), self.var_grade.get(), self.var_id.get()))
            self.conn.commit()
            self.fetch_data()
            messagebox.showinfo("Success", "Record Updated Successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

    def delete_student(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Select a student to delete")
        else:
            self.cursor.execute("DELETE FROM students WHERE id=?", (self.var_id.get(),))
            self.conn.commit()
            self.fetch_data()
            self.clear_fields()
            messagebox.showinfo("Deleted", "Record Deleted Successfully")

    def search_data(self):
        if self.search_txt.get() == "" or self.search_by.get() == "":
            messagebox.showerror("Error", "Search selection and text are required")
        else:
            query = f"SELECT * FROM students WHERE {self.search_by.get().lower()} LIKE '%{self.search_txt.get()}%'"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('', END, values=row)

if __name__ == "__main__":
    root = Tk()
    obj = CollegeManagementSystem(root)
    root.mainloop()