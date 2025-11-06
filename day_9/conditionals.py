# get user age using input 
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to  learn to drive.")
else:
    print(f"You need {18 - age} more years to learn how to drive.")

# compare values of ages 
my_age = int(input("Enter my age: "))
your_age = int(input("Enter your age: "))
if your_age - my_age == 1:
    print(f"Your  are 1 year older than me.")
    if your_age - my_age !=1:
        print(f"You are {your_age - my_age} years older than me.")
else:
    print(f"We are age mates!")

# get numbers from the user
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b: 
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

# students grade based on their scores 
score = int(input("Enter your score: "))
if score >= 80:
    print(f"{score} is A.") 
elif score >= 70 :
    print(f"{score}is B.")
elif score >=60:
    print(f"{score} is C.")
elif score >=50:
    print(f"{score} is D.")
else:
    print(f"{score} is F.")


# check the season 
month = input("Enter month: ").capitalize()
if month in["October" , "September" , "November"]:
    print(f"The month of {month} is Autumn season.")
elif month  in ["December" , "January" , "February"]:
    print(f"The month of {month} is Winter season.")
elif month in["June" , "July" , "August"]:
    print(f"The month of {month} is Summer season.") 
elif month in ["March", "April", "May"]:
    print(f"The month  of {month} is Spring season.")
else:
    print(f"Please enter a valid month!")

# checking and adding fruits in a list 
fruits = ['banana', 'orange', 'mango', 'lime']
if not 'banana' in fruits:
    fruits.append("banana")
else:
    print("That fruit already exists in the list")

# person dictionary 
person = {
    'first_name': 'Byrone',
    'last_name': 'Songa', 
    'age': 30, 
    'country':'Germany',
    'is_married':True,
    'skills':['Python', 'SQL', 'Django', 'Git'],
    'address': {
        'street' :'Munich',
        'zipcode':'02210'
    }
}
if 'skills' in person:
    middle_index = len(person['skills']) //2
    print(person['skills'][middle_index])

# more checking 
if 'Python' in person['skills']:
    print('Python is present')
else:
    print("Python not present")

# conditional nesting 
if  any( skill in ['Python','SQL', 'Django'] for skill in person['skills']):
    print(f"He is a backend developer")
elif  any(skill  in ['JavaScript', 'React'] for skill in person['skills']):
    print(f"He is a frontend developer") 
elif  any( skill in  ['React', 'Node', 'MongoDB']  for skill in person['skills']):
    print(f"He is a full stack developer") 
else:
    print(f"He has unkown title")

# check if the person is married 
if person['is_married'] and person['country']:
    print(f"{person['first_name']} {person['last_name']} lives  in {person['country']}. He is married.")