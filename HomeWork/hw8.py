import sqlite3

conn = sqlite3.connect('person.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Departments (
    DepartmentID INTEGER PRIMARY KEY,
    DepartmentName TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    DepartmentID INTEGER,
    FOREIGN KEY (DepartmentID) REFERENCES Departments (DepartmentID)
)
''')

departments = [
    (101, 'HR'),
    (102, 'IT'),
    (103, 'Sales')
]
cursor.executemany('INSERT INTO Departments (DepartmentID, DepartmentName) VALUES (?, ?)', departments)

employees = [
    ('Alice', 'Johnson', 101),
    ('Bob', 'Smith', 101),
    ('Charlie', 'Brown', 102),
    ('David', 'Wilson', 102),
    ('Emma', 'Davis', 103),
    ('Frank', 'Taylor', 103)
]
cursor.executemany('INSERT INTO Employees (FirstName, LastName, DepartmentID) VALUES (?, ?, ?)', employees)

cursor.execute('''
SELECT Employees.EmployeeID, Employees.FirstName, Employees.LastName, Departments.DepartmentName
FROM Employees
JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID
''')
all_employees = cursor.fetchall()
print("список всех сотрудников с указанием их отделов:")
for emp in all_employees:
    print(emp)

cursor.execute('''
SELECT Employees.EmployeeID, Employees.FirstName, Employees.LastName
FROM Employees
JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID
WHERE Departments.DepartmentName = 'IT'
''')
it_employees = cursor.fetchall()
print("\nсписок сотрудников, работающих в отделе IT:")
for emp in it_employees:
    print(emp)

conn.commit()
conn.close()