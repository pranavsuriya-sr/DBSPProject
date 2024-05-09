import tkinter as tk
import sqlite3
import tkinter.messagebox as mb

# Connecting to the Database
connector = sqlite3.connect('SchoolManagement.db')
cursor = connector.cursor()

# Function to fetch marks based on roll number and email
def fetch_marks():
    roll_no = roll_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not roll_no or not email:
        mb.showerror('Error!', "Please fill all the fields!!")
    else:
        try:
            cursor.execute("SELECT MARKS FROM SCHOOL_MANAGEMENT WHERE ROLL_NO = ? AND EMAIL = ? AND PASSWORD = ?", (roll_no, email, password))
            result = cursor.fetchone()
            if result:
                marks = result[0]
                mb.showinfo('Marks', f"Marks for Roll No: {roll_no} and Email: {email} is {marks}")
            else:
                mb.showerror('Error!', "No record found for the provided Roll No and Email")
        except Exception as e:
            mb.showerror('Error', f'An error occurred: {str(e)}')

# Creating the GUI
root = tk.Tk()
root.title('Fetch Marks')
root.geometry('400x200')

# Roll Number Entry
roll_label = tk.Label(root, text="Roll Number:", font=('Arial', 12))
roll_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
roll_entry = tk.Entry(root, font=('Arial', 12))
roll_entry.grid(row=0, column=1, padx=10, pady=10)

# Email Entry
email_label = tk.Label(root, text="Email:", font=('Arial', 12))
email_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
email_entry = tk.Entry(root, font=('Arial', 12))
email_entry.grid(row=1, column=1, padx=10, pady=10)

password_label = tk.Label(root, text="Password:", font=('Arial', 12))
password_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')
password_entry = tk.Entry(root, font=('Arial', 12))
password_entry.grid(row=2, column=1, padx=10, pady=10)

# Button to fetch marks
fetch_button = tk.Button(root, text="Fetch Marks", command=fetch_marks, font=('Arial', 12))
fetch_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
