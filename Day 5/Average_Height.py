student_heights = input("Plese Enter a list of students height : ").split()
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])
print(student_heights)
count = 0
total = 0
for i in student_heights:
    count += 1
    total += i
average_student_heights = total / count
print(average_student_heights)