import json
import os # operating system
import time

# Function para mag-load ng student data mula sa JSON file
def load_students(filename):
    print("⏳ Loading", end="")  # Mag-print ng "Loading" na walang bagong linya
    for _ in range(3):  # Gagawa ng tatlong dots para magmukhang may loading
        print(".", end="")  # Mag-print ng dot at i-flush para agad lumabas
        time.sleep(1)  # Maghintay ng 1 segundo

    print()  # Mag-print ng new line pagkatapos ng loading dots
    if os.path.exists(filename):  # Check kung may existing na file
        with (open(filename, 'r') as file):
            print("✅ Data loaded successfully.")
            return json.load(file)  # Binabasa ang data mula sa JSON file
    else:
        print("⚠️ No data found. Returning empty list.")
        return []  # Kung walang file, magbabalik ng empty list


# Function para mag-save ng student data sa JSON file
def save_students(filename, students):
    print("💾 Saving", end="")  # Mag-print ng "Saving" na walang bagong linya
    for _ in range(3):  # Magdadagdag ng loading dots
        print(".", end="")  # Mag-print ng dot
        time.sleep(1)# Maghintay ng 1 segundo
    print()  # Mag-print ng new line pagkatapos ng loading dots

    with open(filename, 'w') as file:
        json.dump(students, file, indent=4)  # Ise-save ang list ng students sa JSON file
    print("✅ Data saved successfully.")

# Function para magdagdag ng student
def add_student(students):
    print("\n🎓 Adding a new student:")
    name = input("🔑 Enter student's name: ")
    age = input("🔑 Enter student's age: ")
    grade = input("🔑 Enter student's grade: ")
    major = input("🔑 Enter student's major: ")

    # Create new student object
    student = {
        "name": name,
        "age": age,
        "grade": grade,
        "major": major
    }

    students.append(student)  # Add student to the list
    save_students("students.json", students)  # Save updated list to JSON file
    print(f"\n🎉 {name} added successfully!")

# Function para mag-update ng student
def update_student(students):
    print("\n🔄 Updating a student:")
    name_to_update = input("🔑 Enter the name of the student you want to update: ")
    for student in students:
        if student['name'].lower() == name_to_update.lower():
            print(f"\n🔧 Updating details for {student['name']}")

            student['name'] = input("🔑 Enter new name: ")
            student['age'] = input("🔑 Enter new age: ")
            student['grade'] = input("🔑 Enter new grade: ")
            student['major'] = input("🔑 Enter new major: ")

            save_students("students.json", students)  # Save updated list to JSON file
            print(f"✅ {student['name']}'s details updated successfully!")
            return

    print("\n❌ Student not found!")

# Function para mag-delete ng student
def delete_student(students):
    print("\n🗑️ Deleting a student:")
    name_to_delete = input("🔑 Enter the name of the student you want to delete: ")
    for student in students:
        if student['name'].lower() == name_to_delete.lower():
            students.remove(student)  # Remove student from the list
            save_students("students.json", students)  # Save updated list to JSON file
            print(f"✅ {name_to_delete} deleted successfully!")
            return

    print("\n❌ Student not found!")

# Function para mag-display ng lahat ng students
def display_students(students):
    print("\n👀 Displaying all students:")
    if not students:
        print("⚠️ No students found.")
        return

    print("\n📚 List of Students:")
    for student in students:
        print(f"🧑‍🎓 Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Major: {student['major']}")

# Main function
def main():
    students = load_students("students.json")  # Load the students from JSON file

    while True:
        print("\n===============================")
        print("🌟 Student Management System 🌟")
        print("===============================")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Display Students")
        print("5. Exit")
        print("===============================")

        choice = input("👉 Choose an option: ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            update_student(students)
        elif choice == '3':
            delete_student(students)
        elif choice == '4':
            display_students(students)
        elif choice == '5':
            print("\n👋 Exiting... Goodbye!")
            break
        else:
            print("\n❌ Invalid option, please try again.")

if __name__ == "__main__":
    main()
