from Student import Student

# Crear una lista de diccionarios con información de estudiantes
student_data = [
    {"name": "Juan", "age": 20, "grades": [85, 92, 78]},
    {"name": "María", "age": 21, "grades": [75, 88, 92]},
    {"name": "Pedro", "age": 19, "grades": [95, 90, 87]},
]

# Crear una lista de objetos de la clase Student usando list comprehension
students = [Student(data["name"], data["age"]) for data in student_data]

# Definir umbral para filtrar estudiantes
umbral = 85

# Filtrar estudiantes con nota promedio por encima del umbral usando list comprehension
students_above_umbral = [student for student in students if student.average_grade() >= umbral]

# Crear un diccionario de estudiantes con nota promedio por encima del umbral usando dictionary comprehension
students_above_umbral_dict = {student.name: student for student in students_above_umbral}

# Imprimir información
for student_name, student in students_above_umbral_dict.items():
    print(f"Nombre: {student_name}, Edad: {student.age}, Nota Promedio: {student.average_grade()}")
