# Step 1: Store student information
students = [
    {"name": "Priya", "mark": 92},
    {"name": "Arun", "mark": 78},
    {"name": "Divya", "mark": 59},
    {"name": "Rahul", "mark": 85}
]


# Step 2: Calculate the grade
def get_grade(mark):

    if mark >= 90:
        return "A"

    elif mark >= 80:
        return "B"

    elif mark >= 70:
        return "C"

    elif mark >= 60:
        return "D"

    else:
        return "E"


# Step 3: Add a new student
def add_student():

    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty!")
        return

    try:
        mark = int(input("Enter student mark (0-100): "))

        if mark < 0 or mark > 100:
            print("Invalid mark! Enter between 0 and 100.")
            return

    except ValueError:
        print("Invalid input! Please enter a whole number.")
        return

    students.append({
        "name": name,
        "mark": mark
    })

    print("Student added successfully!")


# Step 4: Display student results
def show_results():

    if len(students) == 0:
        print("No students available!")
        return

    print("\n========== STUDENT RESULTS ==========")

    print(f"{'Name':<15}{'Mark':<10}{'Grade':<10}")
    print("-" * 35)

    for student in students:

        name = student["name"]
        mark = student["mark"]
        grade = get_grade(mark)

        print(f"{name:<15}{mark:<10}{grade:<10}")

    # Calculate class average
    marks = [student["mark"] for student in students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print("-" * 35)

    print(f"Average: {average:.1f}")
    print(f"Highest mark: {highest}")
    print(f"Lowest mark: {lowest}")

    print("=" * 35)


# Step 5: Main menu
while True:

    print("\n===== STUDENT GRADE MANAGER =====")

    print("1. Add Student")
    print("2. Show Results")
    print("3. Quit")

    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":

        add_student()

    elif choice == "2":

        show_results()

    elif choice == "3":

        print("Thank you! Program closed.")
        break

    else:

        print("Invalid choice! Please enter 1, 2 or 3.")
