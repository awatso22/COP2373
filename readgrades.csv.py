import csv

def read_grades():
    print("\nStudnet Grades:\n")

    with open('grades.csv', 'r') as file:
        reader = csv.reader(file)

        # Loop through rows and print formatted output
        for row in reader:
            print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<10}{row[4]:<10}")


