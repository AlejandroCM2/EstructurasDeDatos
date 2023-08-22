from student import Student

student_data = [
    {"name": "Juan", "age": 20, "grades": [85, 92, 78]},
    {"name": "María", "age": 21, "grades": [75, 88, 92]},
    {"name": "Pedro", "age": 19, "grades": [95, 90, 87]},
]

students = [Student(data["name"], data["age"]) for data in student_data]

umbral = 85

students_above_umbral = [student for student in students if student.average_grade() >= umbral]

students_above_umbral_dict = {student.name: student for student in students_above_umbral}

for student_name, student in students_above_umbral_dict.items():
    print(f"Nombre: {student_name}, Edad: {student.age}, Nota Promedio: {student.average_grade()}")
