"""
students = {
    "Hermione":"GRYNFFINDOR", "Harry": "GRINFFINDOR",
            "Ron":"GRINFFINDOR", "Draco":"SLYTHERIN"
}
for student in students:
    print(student, students[student], sep=",")
    
"""

students = [
    {"name":"Hermione", "house":"Grynffindor", "patronus":"Otter"},
    {"name":"Harry", "house":"Grynffindor", "patronus":"Stag"},
    {"name":"Ron", "house":"Grynffindor", "patronus":"Jack Russel terrier"},
    {"name":"Draco", "house":"Slytherin", "patronus":None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=",")