# Lab 6 - Student Grade Calculator
# Menu-driven program to enter and view the grade
# of the most recently entered student.


def get_mark(subject_number):
    """Take and validate marks between 0 and 100."""

    while True:
        try:
            mark = float(input(f"Enter marks for subject {subject_number}: "))

            if 0 <= mark <= 100:
                return mark

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_grade(average):
    """Return the grade according to the given grading scheme."""

    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def grade_calculator():
    """Run the student grade calculator."""

    last_student = None

    while True:
        print("\n===== STUDENT GRADE CALCULATOR =====")
        print("1. Enter marks for a new student")
        print("2. View grade of last entered student")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            marks = []

            for subject in range(1, 6):
                marks.append(get_mark(subject))

            average = sum(marks) / 5
            grade = calculate_grade(average)

            last_student = {
                "marks": marks,
                "average": average,
                "grade": grade
            }

            print("\nStudent data saved successfully.")
            print(f"Average: {average:.2f}")
            print(f"Grade: {grade}")

        elif choice == "2":
            if last_student is None:
                print("No student data has been entered yet.")
            else:
                print("\n===== LAST ENTERED STUDENT =====")
                print("Marks:", *last_student["marks"])
                print(f"Average: {last_student['average']:.2f}")
                print(f"Grade: {last_student['grade']}")

        elif choice == "3":
            print("Exiting Grade Calculator...")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    grade_calculator()