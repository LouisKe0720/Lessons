words = ["python", "java", "c++", "ruby", "javascript", "python", "java", "python", "c++", "python"]
python_count = 0
for word in words:
    if word == "python":
        python_count += 1
print("There are", python_count, "instances of the word 'python' in the list.")