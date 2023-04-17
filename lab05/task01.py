import smtplib
import csv
import os.path

# funkcja do wczytania danych z pliku csv
def load_data(filename):
    data = {}
    if not os.path.isfile(filename):
        return data
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            email, name, surname, points = row[:4]
            graded_status = ""
            mailed_status = ""
            if len(row) > 4:
                graded_status, mailed_status = row[4:]
            data[email] = {
                "name": name,
                "surname": surname,
                "points": int(points),
                "graded_status": graded_status,
                "mailed_status": mailed_status
            }
    return data

# funkcja do zapisu danych do pliku csv
def save_data(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for email, student in data.items():
            writer.writerow([email, student['name'], student['surname'], student['points'], student['graded_status'], student['mailed_status']])

# funkcja do automatycznego wystawienia oceny
def assign_grades(data, max_points):
    for email, student in data.items():
        if student['graded_status'] == "" and student['mailed_status'] == "":
            grade = round(student['points'] / max_points * 5, 1)
            student['graded_status'] = str(grade)

# funkcja do usuwania studenta
def remove_student(data, email):
    if email in data:
        del data[email]

# funkcja do dodawania studenta
def add_student(data, email, name, surname, points):
    if email in data:
        return False
    data[email] = {
        "name": name,
        "surname": surname,
        "points": int(points),
        "graded_status": "",
        "mailed_status": ""
    }
    return True

# funkcja do wysyłania maila
def send_email(server, from_email, password, to_email, subject, message):
    with smtplib.SMTP_SSL(server, 465) as smtp:
        smtp.login(from_email, password)
        msg = f"Subject: {subject}\n\n{message}"
        smtp.sendmail(from_email, to_email, msg)

# funkcja do wysyłania maili z ocenami
def send_grades_email(data, server, from_email, password, max_points):
    for email, student in data.items():
        if student['mailed_status'] == "":
            if student['graded_status'] == "":
                grade = round(student['points'] / max_points * 5, 1)
                student['graded_status'] = str(grade)
            subject = "Ocena z przedmiotu Podstawy Programowania Python"
            message = f"Cześć {student['name']}, Twoja ocena z przedmiotu Podstawy Programowania Python to {student['graded_status']} na 5.\n\nPozdrawiamy,\nZespół P3"
            send_email(server, from_email, password, email, subject, message)
            student['mailed_status'] = "MAILED"

# wczytanie danych z pliku
filename = "students.csv"
data = load_data(filename)

# parametry do wysyłania maili
email_server = "smtp.gmail.com"
email_from = "mojemail@gmail.com"
email_password = "mojehaslo"
max_points = 100

# wysłanie maili z ocenami
send_grades_email(data, email_server, email_from, email_password, max_points)

# zapisanie zmian w pliku csv
save_data(filename, data)

with open("password.txt", "r") as file:
    email_password = file.read().strip()

while True:
    print()
    print("Co chcesz zrobić?")
    print("1. Wystawić oceny")
    print("2. Usunąć studenta")
    print("3. Dodać studenta")
    print("4. Wysłać maile z ocenami")
    print("5. Wyjść z programu")
    choice = input("Wybierz opcję: ")

    if choice == "1":
        assign_grades(data, max_points)
        save_data(filename, data)
        print("Oceny zostały wystawione i zapisane do pliku.")
    elif choice == "2":
        email = input("Podaj email studenta do usunięcia: ")
        remove_student(data, email)
        save_data(filename, data)
        print("Student został usunięty i zapisany do pliku.")
    elif choice == "3":
        email = input("Podaj email nowego studenta: ")
        name = input("Podaj imię nowego studenta: ")
        surname = input("Podaj nazwisko nowego studenta: ")
        points = input("Podaj liczbę punktów nowego studenta: ")
        added = add_student(data, email, name, surname, points)
        if added:
            save_data(filename, data)
            print("Student został dodany i zapisany do pliku.")
        else:
            print("Nie można dodać studenta o takim adresie email.")
    elif choice == "4":
        send_grades_email(data, email_server, email_from, email_password, max_points)
        save_data(filename, data)
        print("Maile z ocenami zostały wysłane i zapisane do pliku.")
    elif choice == "5":
        break
    else:
        print("Niepoprawna opcja, spróbuj ponownie.")
