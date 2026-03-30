import csv

def write_grades():
    num_students = int(input('Enter number of students: '))

    with open('grades.csv', 'a') as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        # Loop through each student
        for i in range(num_students):
            print(f"\nEntering data for student {i+1}.")

            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')

            exam_1 = input('Enter exam 1: ')
            exam_2 = input('Enter exam 2: ')
            exam_3 = input('Enter exam 3: ')

            # Write row to CSV
            writer.writerow([first_name, last_name, exam_1, exam_2, exam_3])

print("\nData successfully written to 'grades.csv'")
