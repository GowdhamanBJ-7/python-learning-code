student = {
    "name": "prakash",
    "age": 56,
    "grade": "A"
}

#Accessing Values
print(student["name"])      # prakash
print(student.get("age"))   # 56

#modifying values
student['age'] = 25
student['city']='Hosur'
print(student)  #{'name': 'prakash', 'age': 25, 'grade': 'A', 'city': 'Hosur'}

#removing elements
student.pop("age")            # Removes 'age'
print(student) #{'name': 'prakash', 'grade': 'A', 'city': 'Hosur'}
del student["grade"]          # Removes 'grade'
print(student) #{'name': 'prakash', 'city': 'Hosur'}
student.clear()               # Clears the dictionary
print(student) #{}


student = {"name": "kumar", "age": 20, "course": "CS"}

print(student.keys())     # dict_keys(['name', 'age', 'course'])
print(student.values())   # dict_values(['Bob', 20, 'CS'])
print(student.items())    # dict_items([('name', 'Bob'), ('age', 20), ('course', 'CS')])

for key, value in student.items():
    print(key, value)
# name kumar
# age 20
# course CS


students = {
    "101": {"name": "Arun", "marks": 85},
    "102": {"name": "babu", "marks": 90}
}

print(students["102"]["name"])  # babu



#update
person = {"name": "Arun", "age": 25}
update_info = {"age": 20, "city": "Hosur"} #{'name': 'Arun', 'age': 20, 'city': 'Hosur'}

person.update(update_info)
print(person)

student = {"name": "Bob", "age": 20}
age = student.pop("age")

print(age)       # 20
print(student)   # {'name': 'Bob'}

result = student.pop("grade", "Not Found")
print(result)  # Not Found

student.clear()
print(student)   # {}
