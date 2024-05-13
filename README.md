# STUDENTS MARK MANAGEMENT SYSTEM

## Problem Statement:
Design and develop a comprehensive Student Mark Management System that facilitates efficient management of student academic records, assessments, attendance, and related information for educational institutions. The system is capable of providing separate interfaces for students, faculty, and administrators, ensuring secure access to relevant features and data

## ENTITY:
Students:
 	Name, roll number, semester, email_address
Course:
	Name, years
Subject:
	Subject_code,credits 	
Teacher:
	Name, teacher_id, title
Department:
	 Department_id, Department_name
Student login:
	Roll_number, Password, Email_address
Teacher login:
	User_name, Password, email_address
Marks:
	Internal, external, Total marks, Subject ID, Roll Number

## RELATIONSHIPS:
•	Course - Student (Many - One)
•	Student - Student Login (One - One)
•	Marks - Student Login (Many - One)
•	Marks - Teacher Login (Many - Many)
•	Teacher - Teacher Login (Many - Many)
•	Student - Department (One - One)
