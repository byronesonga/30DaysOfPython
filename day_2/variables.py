# Day 2: 30 Days of Python Programming 

# first name 
first_name = "Byrone" 
print(type(first_name))

# last name 
last_name = "Songa"
print(type(last_name))

# full_name 
full_name = "Byrone Songa"
print(type(full_name))

# country
country = "Kenya"
print(type(country))

# city 
city = "Kisumu"
print(type(city))

# age 
age = 30 
print(type(age))

# year 
year = 1995 
print(type(age))

# is married
is_married = True
print(type(is_married))

# is true 
is_true = True 
print(type(is_true))

# is light on 
is_light_on = False 
print(type(is_light_on))

# multiple variables 
first_name, last_name, full_name, country, city, age, year, is_married, is_light_on, is_true = "Byrone", "Songa", "Byrone Songa", "Kenya", "Kisumu", 30, 1995, True, True, False

# length of first name 
print(len(first_name))

# lenghth of last name 
print(len(last_name))

# diffrence in lenght of first name and last name 
print(len(first_name) - len(last_name))

# declare variables of two numbers 
num_one = 5 
num_two = 4 

# add the numbers 
total = (num_one + num_two)
print(total)

# subtract the numbers 
diff = (num_one - num_two)
print(diff)

# multply the numbers 
product = (num_one * num_two)
print(product)

# divide the numbers 
division = (num_one / num_two)
print(division) 

# modulus operation of the two numbers 
remainder = (num_one % num_two) 
print(remainder)

# expoenantion of the numbers 
exp = (num_one ** num_two)
print(exp)

# floor division of the numbers 
floor_division = (num_one // num_two)
print(floor_division)

# area of a cicrcle 
import math 
radius = 30 
area_of_circle = math.pi * radius ** 2 
print(f"The area is: {area_of_circle:.2f}")

# circumference  of a circle 
import math 
radius = 30 
circum_of_circle = 2 * math.pi * radius 
print(f"The circumference is: {circum_of_circle:.2f}")

# user input 
import math 
rad = int(input("Enter radius of the circle: "))
area_circle = math.pi * rad * rad 
print(f"The area of the circle is:{area_circle:.2f}")

# user input 
your_first_name = input("Enter your first name: ")
your_last_name = input("Enter your last name: ")
your_country = input("Enter your country: ")
your_age = input("Enter your age: ") 

# python keywords 
help("keywords")