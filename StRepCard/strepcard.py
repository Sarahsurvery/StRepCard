def calculate_grade(percentage):
    if percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "F"

def get_student_data():
    students = []
    while True:
        name = input("Enter Student Name: ")
        roll_number = input("Enter Roll Number: ")
        subjects = ['Math', 'Physics', 'Urdu', 'English', 'Computer']
        marks = {}
        
        for subject in subjects:
            mark = input(f"Enter marks obtained in {subject} (0-100): ")
            while not mark.isdigit() or not (0 <= int(mark) <= 100):
                print("Invalid input. Please enter a number between 0 and 100.")
                mark = input(f"Enter marks obtained in {subject} (0-100): ")
            marks[subject] = int(mark)
        
        students.append({
            'name': name,
            'roll_number': roll_number,
            'marks': marks
        })
        
        print(f"Record of {name} inserted successfully.")
        cont = input("Do you want to insert more? (Y/N): ").strip().upper()
        while cont not in ['Y', 'N']:
            cont = input("Invalid input. Please enter Y or N: ").strip().upper()
        if cont == 'N':
            break
    return students

def generate_report_card(students):
    print("\nStudent Report Cards")
    print("=" * 50)
    for student in students:
        total_marks = sum(student['marks'].values())
        percentage = total_marks / 5
        grade = calculate_grade(percentage)
        
        print(f"\nStudent Name: {student['name']}")
        print(f"Roll Number: {student['roll_number']}")
        for subject, mark in student['marks'].items():
            print(f"{subject}: {mark}")
        print(f"Total Marks: {total_marks}/500")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")
        print("-" * 50)

def main():
    students = get_student_data()
    generate_report_card(students)

if __name__ == "__main__":
    main()
