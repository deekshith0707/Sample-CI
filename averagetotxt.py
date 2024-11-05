# List of students with their grades
students = [
    {"name": "Alice", "grades": [85, 92, 78]},
    {"name": "Bob", "grades": [79, 85, 88]},
    {"name": "Charlie", "grades": [92, 95, 89]},
    {"name": "Diana", "grades": [70, 75, 80]}
]

# Function to calculate the average grade
def calculate_average(grades):
    return sum(grades) / len(grades)

# Open a text file to write the results
with open("student_averages.txt", "w") as file:
    # Write header
    file.write("Student Average Grades:\n")
    file.write("========================\n")
    
    # Calculate and write average for each student
    for student in students:
        average = calculate_average(student["grades"])
        file.write(f"{student['name']}: {average:.2f}\n")

print("Average grades have been written to 'student_averages.txt'.")