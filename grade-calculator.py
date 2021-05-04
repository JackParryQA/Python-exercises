grade="D"
math = int(input("What was your Maths mark? "))
chem = int(input("What was your Chemistry mark? "))
phys = int(input("What was your Physics mark? "))

total_marks=(math+chem+phys)/3

print(f"Your percentage score is: {total_marks}")

if total_marks>=50 and total_marks<60:
    grade="C"
elif total_marks>=60 and total_marks<70:
    grade="B"
elif total_marks>=70:
    grade="A"

print(f"You scored a grade of: {grade}")