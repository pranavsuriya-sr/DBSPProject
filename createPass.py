import tkinter as tk
import sqlite3
import tkinter.messagebox as mb

# Connecting to the Database
connector = sqlite3.connect('SchoolManagement.db')
cursor = connector.cursor()

# Creating the table if not exists
cursor.execute(
    "CREATE TABLE IF NOT EXISTS SCHOOL_MANAGEMENT (STUDENT_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "
    "NAME TEXT, EMAIL TEXT, ROLL_NO TEXT, GENDER TEXT, DOB TEXT, STREAM TEXT, MARKS TEXT, PASSWORD TEXT)"
)

# Function to add password based on roll number
def add_password():
    roll_no = roll_entry.get()
    password = password_entry.get()

    if not roll_no or not password:
        mb.showerror('Error!', "Please fill all the fields!!")
    else:
        try:
            # Check if the roll number exists
            cursor.execute("SELECT * FROM SCHOOL_MANAGEMENT WHERE ROLL_NO = ?", (roll_no,))
            result = cursor.fetchone()
            if result:
                # Update password if roll number exists
                cursor.execute("UPDATE SCHOOL_MANAGEMENT SET PASSWORD = ? WHERE ROLL_NO = ?", (password, roll_no))
                connector.commit()
                mb.showinfo('Success', f"password {password} added for Roll No: {roll_no}")
            else:
                mb.showerror('Error', "Roll number not found! Create student first.")
        except Exception as e:
            mb.showerror('Error', f'An error occurred: {str(e)}')

# Creating the GUI
root = tk.Tk()
root.title('Add password')
root.geometry('400x200')

# Roll Number Entry
roll_label = tk.Label(root, text="Roll Number:", font=('Arial', 12))
roll_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
roll_entry = tk.Entry(root, font=('Arial', 12))
roll_entry.grid(row=0, column=1, padx=10, pady=10)

# password Entry
password_label = tk.Label(root, text="password:", font=('Arial', 12))
password_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
password_entry = tk.Entry(root, font=('Arial', 12))
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Button to add password
add_button = tk.Button(root, text="Add password", command=add_password, font=('Arial', 12))
add_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
