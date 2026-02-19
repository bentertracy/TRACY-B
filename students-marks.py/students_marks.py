# student_marks.py
# Prompt the user to enter five subject marks
marks = []
for i in range(5):
    mark = float(input(f"Enter mark {i+1}: "))
    marks.append(mark)
# Calculate total and average
total = sum(marks)
average = total / 5

# Determine grade
if average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "E"

# Display results
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)