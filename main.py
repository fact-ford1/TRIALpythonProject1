score = int(input("ENTER YOUR EXAMS SCORE="))
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
elif 50 <= score <= 59:
    grade = "E"
elif 0 <= score <= 49:
    grade = "F"
print()
print(grade)
