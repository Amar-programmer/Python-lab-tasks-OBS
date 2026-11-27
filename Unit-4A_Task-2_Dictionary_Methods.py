
student = {
    "name": "Amardeep",
    "age": 19,
    "course": "Python"
}

print("Keys:", student.keys())

print("Values:", student.values())

print("Items:", student.items())

print("Name:", student.get("name"))

student.update({"age": 19})
print("After Update:", student)

student.pop("course")
print("After Pop:", student)

student.popitem()
print("After Popitem:", student)

student.setdefault("city", "Hyderabad")
print("After Setdefault:", student)

new_student = student.copy()
print("Copied Dictionary:", new_student)

new_student.clear()
print("After Clear:", new_student)