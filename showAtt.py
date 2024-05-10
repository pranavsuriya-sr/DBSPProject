import tkinter as tk
import sqlite3
import tkinter.messagebox as mb

# Connecting to the Database
connector = sqlite3.connect('SchoolManagement.db')
cursor = connector.cursor()

# Function to fetch marks based on roll number and stream
def fetch_marks():
    roll_no = roll_entry.get()
    stream = stream_entry.get()

    if not roll_no or not stream:
        mb.showerror('Error!', "Please fill all the fields!!")
    else:
        try:
            cursor.execute("SELECT ATTENDANCEPERC FROM ATTENDANCE WHERE ROLL_NO = ? AND STREAM = ?", (roll_no, stream))
            result = cursor.fetchone()
            if result:
                attendance = result[0]
                mb.showinfo('ATTENDANCE', f"ATTENDANCE for Roll No: {roll_no} and stream: {stream} is {attendance}")
            else:
                mb.showerror('Error!', "No record found for the provided Roll No and stream")
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

# stream Entry
stream_label = tk.Label(root, text="stream:", font=('Arial', 12))
stream_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
stream_entry = tk.Entry(root, font=('Arial', 12))
stream_entry.grid(row=1, column=1, padx=10, pady=10)

# Button to fetch marks
fetch_button = tk.Button(root, text="Fetch Marks", command=fetch_marks, font=('Arial', 12))
fetch_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
