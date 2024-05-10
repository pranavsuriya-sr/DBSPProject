import tkinter as tk
import sqlite3
import tkinter.messagebox as mb

# Connecting to the Database
connector = sqlite3.connect('Attendance.db')
cursor = connector.cursor()

# Creating the table if not exists
cursor.execute(
    "CREATE TABLE IF NOT EXISTS ATTENDANCE (ATT_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,ROLL_NO TEXT, STREAM TEXT, ATTENDANCEPERC TEXT)"
)

# Function to add attendance based on roll number
def add_attendance():
    roll_no = roll_entry.get()
    attendance = attendance_entry.get()
    stream = stream_entry.get()

    if not roll_no or not attendance or not stream:
        mb.showerror('Error!', "Please fill all the fields!!")
    else:
        try:

                # Update attendance if roll number exists
                cursor.execute("INSERT INTO ATTENDANCE (ROLL_NO, STREAM, ATTENDANCEPERC) VALUES (?,?,?)", (roll_no, stream, attendance))
                connector.commit()
                mb.showinfo('Success', f"Attendace {attendance} added for Roll No: {roll_no}")
        except Exception as e:
            mb.showerror('Error', f'An error occurred: {str(e)}')

# Creating the GUI
root = tk.Tk()
root.title('Add attendance')
root.geometry('400x200')

# Roll Number Entry
roll_label = tk.Label(root, text="Roll Number:", font=('Arial', 12))
roll_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
roll_entry = tk.Entry(root, font=('Arial', 12))
roll_entry.grid(row=0, column=1, padx=10, pady=10)

# attendance Entry
attendance_label = tk.Label(root, text="attendance:", font=('Arial', 12))
attendance_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
attendance_entry = tk.Entry(root, font=('Arial', 12))
attendance_entry.grid(row=1, column=1, padx=10, pady=10)

stream_label = tk.Label(root, text="STREAM:", font=('Arial', 12))
stream_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')
stream_entry = tk.Entry(root, font=('Arial', 12))
stream_entry.grid(row=2, column=1, padx=10, pady=10)

# Button to add attendance
add_button = tk.Button(root, text="Add attendance", command=add_attendance, font=('Arial', 12))
add_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
