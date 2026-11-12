name = input("Student Name: ")

sub1 = int(input("Enter marks for subject 1: "))
sub2 = int(input("Enter marks for subject 2: "))
sub3 = int(input("Enter marks for subject 3: "))

total_marks = sub1 + sub2 + sub3
average_marks = total_marks / 3

if 80 <= average_marks <= 100:
    Grade = "A+"
elif 70 <= average_marks <80:
    Grade = "A"
elif 60 <= average_marks <70:
    Grade = "B"
elif 50 <= average_marks <60:
    Grade = "C"
else:
    Grade = "F"


    
print(f"\nStudent Name: {name} ")
print(f"total marks: {total_marks} ")
print(f"Average: {average_marks:.2f}")
print(f"Grade: {Grade} ")
