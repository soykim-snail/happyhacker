classroom = {
    'teacher': 'kim',
    'student1': 'hong',
    'student2': 'choi'
}

# key를 추출한다
for member in classroom:
    print(member) # key

# value를 추출한다
for member in classroom:
    print(classroom[member]) # value

# keys
for member in classroom.keys():
    print(member) # key

# values
for member in classroom.values():
    print(member) # value

# items
for key, value in classroom.items():
    print(key, value) # tuple

