student = {
    "name": "Lerato",
    "age": 21,
    "major": "Computer Science"
}

student["age"] = 22
student["grade"] = "A"

for key, value in student.items():
    print(f"{key}: {value}")

