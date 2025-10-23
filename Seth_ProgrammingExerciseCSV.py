#This program allows you to input how many students they want to enter. Then enter each student’s first name and last name
#with the student’s three exam grades as integers and displays it in a CSV file.
import csv


def write_grades_to_csv():

    try:
        num_students = int(input("Enter the number of students to enter: "))
    except ValueError:
        print("Invalid input. Please enter an integer for the number of students.")
        return

    with open('grades.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])  # Header

        for i in range(num_students):
            print(f"\nEntering data for student {i + 1}:")
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")

            grades = []
            for j in range(1, 4):
                while True:
                    try:
                        grade = int(input(f"Enter grade for Exam {j}: "))
                        grades.append(grade)
                        break
                    except ValueError:
                        print("Invalid input. Please enter an integer for the grade.")

            writer.writerow([first_name, last_name] + grades)
    print("\nStudent grades successfully written to grades.csv")


if __name__ == "__main__":
    write_grades_to_csv()

import csv

def display_grades_from_csv():

    try:
        with open('grades.csv', 'r') as file:
            reader = csv.reader(file)
            header = next(reader)

            col_widths = [len(h) for h in header]
            data = []
            for row in reader:
                data.append(row)
                for i, item in enumerate(row):
                    if len(item) > col_widths[i]:
                        col_widths[i] = len(item)

            header_format = " ".join([f"{{:<{w}}}" for w in col_widths])
            print(header_format.format(*header))
            print("-" * (sum(col_widths) + len(col_widths) - 1)) # Separator line

            for row in data:
                print(header_format.format(*row))

    except FileNotFoundError:
        print("Error: grades.csv not found. Please ensure the file exists.")
    except StopIteration:
        print("Error: grades.csv is empty or only contains a header.")

if __name__ == "__main__":
    display_grades_from_csv()
