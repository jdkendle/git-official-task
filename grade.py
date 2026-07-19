score_text = input("Enter your score: ")
score = int(score_text)

if score >= 90:
    grade = "A"
    message = "Excellent work"
elif score >= 89:
    grade = "B"
    message = "B Good job "
elif score >= 70:
    grade = "C"
    message = "C You passed"
elif score >= 60:
    grade = "D"
    message = "D You passed barely --- needs improvement. "
else:
    grade = "F"
    message = "You did not pass."

print(f"Grade = {grade} - {message}")
