import csv
import smtplib
from email.mime.text import MIMEText

class StudentManagementSystem:
    def __init__(self, data_file):
        self.data_file = data_file
        self.students = self.load_data()

    def load_data(self):
        students = {}
        with open(self.data_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                email, first_name, last_name, points, grade, status = row
                students[email] = {
                    'email': email,
                    'first_name': first_name,
                    'last_name': last_name,
                    'points': int(points),
                    'grade': grade,
                    'status': status
                }
        return students

    def save_data(self):
        with open(self.data_file, 'w', newline='') as file:
            writer = csv.writer(file)
            for student in self.students.values():
                writer.writerow([
                    student['email'],
                    student['first_name'],
                    student['last_name'],
                    str(student['points']),
                    student['grade'],
                    student['status']
                ])

    def add_student(self, email, first_name, last_name):
        if email in self.students:
            print("Student with this email already exists.")
            return

        self.students[email] = {
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'points': 0,
            'grade': '',
            'status': ''
        }
        self.save_data()
        print(f"Student {email} added successfully.")

    def remove_student(self, email):
        if email in self.students:
            del self.students[email]
            self.save_data()
            print(f"Student {email} removed successfully.")
        else:
            print("Student with this email does not exist.")

    def grade_students(self, passing_points, grade):
        for student in self.students.values():
            if student['status'] not in ['GRADED', 'MAILED']:
                if student['points'] >= passing_points:
                    student['grade'] = grade
                    student['status'] = 'GRADED'
                else:
                    student['grade'] = ''
                    student['status'] = ''
        self.save_data()
        print("Grading completed successfully.")

    def send_grade_emails(self, smtp_server, smtp_port, sender_email, sender_password):
        for student in self.students.values():
            if student['status'] != 'MAILED':
                message = f"Dear {student['first_name']},\n\n" \
                          f"We are pleased to inform you that your grade for the Python Programming Basics " \
                          f"course has been assigned. Your grade is: {student['grade']}.\n\n" \
                          f"Best regards,\n" \
                          f"Your University"
                msg = MIMEText(message)
                msg['Subject'] = "Grade Notification"
                msg['From'] = sender_email
                msg['To'] = student['email']

                try:
                    with smtplib.SMTP(smtp_server, smtp_port) as server:
                        server.starttls()
                        server.login(sender_email, sender_password)
                        server.sendmail(sender_email, student['email'], msg.as_string())
                    student['status'] = 'MAILED'
                except smtplib.SMTPException as e:
                    print(f"An error occurred while sending an email to {student['email']}: {str(e)}")

        self.save_data()
        print("Emails sent successfully.")

# Przykład użycia:
sms = StudentManagementSystem('students.csv')
sms.add_student('student1@example.com', 'John', 'Doe')
sms.add_student('student2@example.com', 'Jane', 'Smith')
