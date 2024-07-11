# students = ["Herimone", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]


# students = {
#       "Hermione": "Gryffinodr",
#       "Harry":"Gryffindor",
#       "Ron": "Gryffindor",
#       "dracco": "slytheirn"
#       }

# print(students["Hermione"])

# for student in students:
#    a = student
#    print(a)

# for student in students:
#     print(student , students[student], sep=", ")

students  = [
    {"name": "Hermione", "house":"Gryffindior", "patronous":"otter"},
    {"name": "Harry", "house":"Gryffindior", "patronous":"stag"},
    {"name": "Ron", "house":"Gryffindior", "patronous":"Jack russel terrier"},
    {"name": "Hermione", "house":"Slytherin", "patronous":None},
]

for student in students:
    print(student["name"],student["house"], student["patronous"], sep=", ")
