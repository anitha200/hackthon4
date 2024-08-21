import sqlite3
from datetime import datetime

# Database setup
def create_tables():
    conn = sqlite3.connect('vaccination_system.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS children (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date_of_birth TEXT NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS vaccinations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            child_id INTEGER,
            vaccine_name TEXT NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY (child_id) REFERENCES children (id)
        )
    ''')
    conn.commit()
    conn.close()

# Function to add a new child
def add_child(name, date_of_birth):
    conn = sqlite3.connect('vaccination_system.db')
    c = conn.cursor()
    c.execute('INSERT INTO children (name, date_of_birth) VALUES (?, ?)', (name, date_of_birth))
    conn.commit()
    conn.close()
    print("Child added successfully.")

# Function to add vaccination record
def add_vaccination(child_id, vaccine_name, date):
    conn = sqlite3.connect('vaccination_system.db')
    c = conn.cursor()
    c.execute('INSERT INTO vaccinations (child_id, vaccine_name, date) VALUES (?, ?, ?)', (child_id, vaccine_name, date))
    conn.commit()
    conn.close()
    print("Vaccination record added successfully.")

# Function to view all children
def view_children():
    conn = sqlite3.connect('vaccination_system.db')
    c = conn.cursor()
    c.execute('SELECT * FROM children')
    children = c.fetchall()
    conn.close()
    print("Children:")
    for child in children:
        print(f"ID: {child[0]}, Name: {child[1]}, Date of Birth: {child[2]}")

# Function to view vaccinations for a child
def view_vaccinations(child_id):
    conn = sqlite3.connect('vaccination_system.db')
    c = conn.cursor()
    c.execute('SELECT * FROM vaccinations WHERE child_id = ?', (child_id,))
    vaccinations = c.fetchall()
    conn.close()
    print(f"Vaccinations for child ID {child_id}:")
    for vac in vaccinations:
        print(f"ID: {vac[0]}, Vaccine Name: {vac[2]}, Date: {vac[3]}")

# CLI for user interaction
def main():
    create_tables()
    while True:
        print("\nChild Vaccination Management System")
        print("1. Add Child")
        print("2. Add Vaccination")
        print("3. View All Children")
        print("4. View Vaccinations for a Child")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter child's name: ")
            date_of_birth = input("Enter child's date of birth (YYYY-MM-DD): ")
            add_child(name, date_of_birth)
        elif choice == '2':
            view_children()
            child_id = int(input("Enter child's ID to add vaccination: "))
            vaccine_name = input("Enter vaccine name: ")
            date = input("Enter date of vaccination (YYYY-MM-DD): ")
            add_vaccination(child_id, vaccine_name, date)
        elif choice == '3':
            view_children()
        elif choice == '4':
            child_id = int(input("Enter child's ID to view vaccinations: "))
            view_vaccinations(child_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
