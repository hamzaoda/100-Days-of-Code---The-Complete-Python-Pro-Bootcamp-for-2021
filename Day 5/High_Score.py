student_scores = input("Plese Enter a list of students score : ").split()
for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])
print(student_scores)

max_score=0
for i in student_scores:
    if max_score < i:
        max_score = i
print(f"the highst score in the class is : {max_score}")