# create empty dictionary 
dog = {}

# add name, color, breed, legs, age to the dog dictionary 
dog = {'name':'Bosco', 'color':'black', 'breed':'German Shephard', 'legs':4, 'age':5}
print(dog)

# create a student dictionary 
student = {'first_name':'Byrone', 'last_name':'Songa', 'gender':'male','age':30, 'marital_status':True ,'skills':['Python', 'SQL', 'Django'], 'country':'Germany', 'address':{
    'street':'Oginga Odinga',
    'zipcode':'02210'
}}
print(student)

# length of student dictionary 
print(len(student))

# get the values of skills 
print(student['skills'])

# check the data type of the values of the skills 
print(type(student['skills']))

# modify the skills values 
student['skills'].append ('Git')
print(student)

# dictionary as keys  list 
print(student.keys())

# dictionary values as list 
print(student.values())

# change dictionary to a list of tuples 
dictonary_list = student.items()
print(dictonary_list) 

# delete one of the items 
student.pop('age')
print(student)

# delete one of dictionaries 
del dog 