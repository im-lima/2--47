import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    hobby TEXT,
    birth_year INTEGER,
    homework_score INTEGER
)
''')

students_data = [
    ('Akylai', 'Tashtandiyeva', 'Dancing', 2004, 10),
    ('Baitikkhan', 'Djunusov', 'Photography', 2000, 10),
    ('Alexandr', 'Gorbin', 'Volleyball', 2006, 5),
    ('Katerina', 'Petrova', 'Swimming', 2002, 9),
    ('Omur', 'Djanybekov', 'Reading', 1997, 8),
    ('Damon', 'Salvatore', 'Gaming', 2001, 10),
    ('Paul', 'Wesley', 'Painting', 2001, 7),
    ('Elena', 'Gilbert', 'Cycling', 2000, 6),
    ('Ian', 'Somerhalder', 'Chess', 2002, 5),
    ('Teahyung', 'Kim', 'Singing', 1995, 10)
]

cursor.executemany('''
INSERT INTO student (first_name, last_name, hobby, birth_year, homework_score)
VALUES (?, ?, ?, ?, ?)
''', students_data)
conn.commit()

cursor.execute('SELECT * FROM student WHERE LENGTH(last_name) > 10')
long_last_name_students = cursor.fetchall()
print("студенты с фамилией больше 10 символов:")
for student in long_last_name_students:
    print(student)

cursor.execute("UPDATE student SET first_name = 'genius' WHERE homework_score > 10")
conn.commit()

cursor.execute("SELECT * FROM student WHERE first_name = 'genius'")
genius_students = cursor.fetchall()
print("\nстуденты с именем 'genius':")
for student in genius_students:
    print(student)

cursor.execute("DELETE FROM student WHERE id % 2 = 0")
conn.commit()

cursor.execute("SELECT * FROM student")
remaining_students = cursor.fetchall()
print("\nоставшиеся студенты после удаления с четными id:")
for student in remaining_students:
    print(student)

conn.close()