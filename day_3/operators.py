# my age 
my_age = 30 

# my heght 
my_height = 3.5

# complex number 
complex_number = 1 + 1j
print(type(complex_number))

# calculating the area of a triangle 
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = int(0.5 * base * height)
print("The area of the triangle is", area)

# calculating the perimeter of a triangle 
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter = int(side_a + side_b + side_c) 
print("The perimeter of the triangle is", perimeter)

# calculating the area of the rectangle 
length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = int(length * width) 
perimeter = int( 2 * (length * width)) 
print("The area of rectangle is", area) 
print("The perimeter of rectangle is", perimeter)

# Caculating the area  of a circle 
radius = int(input("Enter radius of a circle: "))
area = int(3.14 * radius * radius)
print("The area of a circle is", area)

# Calculating the circumference of a circle 
circumference = int(2 * 3.14 * radius)
print("The circumfernce of a circle is", circumference)

# length of dragon and python 
print(len("dragon"))
print(len("python"))
print(len("dragon")  > len("python")) 

# check on using and operator 
print("on" in "python" and "on" in "dragon")
print("on" not in "python" and "on" not in "dragon")

# check jargon in a sentence 
print("jargon" in "I hope this course is not full of jargon")

# check the value of text python 
text = "python" 
print(len(text))
print(int(len(text)))
print(float(len(text)))

# check even numbers 
even_number = int(input("Enter a number: "))
if even_number % 2 == 0:
    print(even_number, "is even number")
else:
    print(even_number, "is odd number")

# check floor division  and int values if they are equal
print(int(2.7) == 7 / 3)

# check if type of string equal to type of int 
print(type('10') == type(10))

# check if float converted to int equal to int 
print(int(9.8)== 10)

# prompt user to enter hours 
hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour 
print(f"Your weekly earning is {weekly_earning}")

# prompt user to enter seconds 
years = int(input("Enter number of years you have lived: "))
seconds_lived = years * 31536000 
print(f"You have lived for {seconds_lived} seconds")

# display a table 
for i in range(1,6):
    print(f"{i:6d} {1:6d} {i**2:6d} {i**3:6d}")