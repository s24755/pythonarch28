import sqlite3
from tkinter import Tk, Label, Entry, Button, messagebox

# Funkcja tworząca tabelę, jeśli nie istnieje
def create_table():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)")
    conn.commit()
    conn.close()

# Funkcja dodająca nowego studenta
def add_student():
    name = name_entry.get()
    grade = grade_entry.get()

    if name and grade:
        conn = sqlite3.connect("students.db")
        c = conn.cursor()
        c.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (name, grade))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sukces", "Dodano studenta.")
    else:
        messagebox.showwarning("Błąd", "Wprowadź imię i ocenę studenta.")

# Funkcja wyświetlająca wszystkich studentów
def display_students():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    rows = c.fetchall()
    conn.close()

    if rows:
        student_list = "\n".join([f"ID: {row[0]}, Imię: {row[1]}, Ocena: {row[2]}" for row in rows])
        messagebox.showinfo("Studenci", student_list)
    else:
        messagebox.showinfo("Studenci", "Brak zapisanych studentów.")

# Funkcja usuwająca studenta o podanym ID
def delete_student():
    student_id = student_id_entry.get()

    if student_id:
        conn = sqlite3.connect("students.db")
        c = conn.cursor()
        c.execute("DELETE FROM students WHERE id=?", (student_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sukces", "Usunięto studenta.")
    else:
        messagebox.showwarning("Błąd", "Wprowadź ID studenta do usunięcia.")

# Funkcja edytująca ocenę studenta o podanym ID
def edit_student_grade():
    student_id = student_id_entry.get()
    new_grade = new_grade_entry.get()

    if student_id and new_grade:
        conn = sqlite3.connect("students.db")
        c = conn.cursor()
        c.execute("UPDATE students SET grade=? WHERE id=?", (new_grade, student_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sukces", "Edytowano ocenę studenta.")
    else:
        messagebox.showwarning("Błąd", "Wprowadź ID studenta i nową ocenę.")

# Tworzenie tabeli (jeśli nie istnieje)
create_table()

# Tworzenie głównego okna
root = Tk()
root.title("Aplikacja studencka")

# Etykiety i pola tekstowe
name_label = Label(root, text="Imię Nazwisko:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

grade_label = Label(root, text="Ocena:")
grade_label.grid(row=1, column=0, padx=10, pady=5)
grade_entry = Entry(root)
grade_entry.grid(row=1, column=1, padx=10, pady=5)

student_id_label = Label(root, text="ID studenta:")
student_id_label.grid(row=2, column=0, padx=10, pady=5)
student_id_entry = Entry(root)
student_id_entry.grid(row=2, column=1, padx=10, pady=5)

new_grade_label = Label(root, text="Nowa ocena:")
new_grade_label.grid(row=3, column=0, padx=10, pady=5)
new_grade_entry = Entry(root)
new_grade_entry.grid(row=3, column=1, padx=10, pady=5)

# Przyciski
add_button = Button(root, text="Dodaj studenta", command=add_student)
add_button.grid(row=4, column=0, padx=10, pady=5)

display_button = Button(root, text="Wyświetl studentów", command=display_students)
display_button.grid(row=4, column=1, padx=10, pady=5)

delete_button = Button(root, text="Usuń studenta", command=delete_student)
delete_button.grid(row=5, column=0, padx=10, pady=5)

edit_button = Button(root, text="Edytuj ocenę studenta", command=edit_student_grade)
edit_button.grid(row=5, column=1, padx=10, pady=5)

root.mainloop()
