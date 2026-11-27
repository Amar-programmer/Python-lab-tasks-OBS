# Unit 4A - Task 1: Create Access Update Dictionary
student = {
    "name": "Amardeep",
    "age": 19,
    "course": "Python",
    "city": "Vijayawada"
}

print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Student Course:", student["course"])

student["age"] = 19
student["course"] = "Java Script"

student["college"] = "Dr.RVR Nri Institute Of Technology,Deemed To Be UNIVERSITY."

print("\nUpdated Dictionary:")
print(student)
