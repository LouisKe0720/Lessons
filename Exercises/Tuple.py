student_info = ("Wayne", 21, "Computer Science", 3.8)
print("Name: " + str(student_info[0]))
print("Age: " + str(student_info[1]))
print("Major: " + str(student_info[2]))
print("GPA: " + str(student_info[3]))

update_student_info = list(student_info)
update_student_info[2] = "Data Science"
updated_student_info = tuple(update_student_info)
print("Updated Student Information: " + str(updated_student_info))

#Task 2

scores = (88, 76, 90, 85, 93, 76, 90, 88, 92)
print(max(scores))
print(min(scores))
print(scores.count(90))
print(sum(scores) / len(scores))

scores = tuple(reversed(sorted((set(scores)))))
print(scores)
print(scores[0])
print(scores[1])
print(scores[2])

