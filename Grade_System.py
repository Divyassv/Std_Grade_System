def calculate_grade(mark):
    if mark > 100:
        raise ValueError("Mark cannot be greater than 100.")
    elif mark >= 90:
        return 'A'
    elif mark >= 80:
        return 'B'
    elif mark >= 70:
        return 'C'
    elif mark >= 60:
        return 'D'
    elif mark <60:
        return 'E'



mark = input("Enter your Marks: ")
try:
    grade = calculate_grade(float(mark))
    print(f"Mark: {mark} Your Grade is: {grade}")
except Exception as e:
    print(f"Error: {e}")