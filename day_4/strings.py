# concatenate string "Thirty", "Days", "Of", "Python"
challenge = "Thirty" + " " "Days" +" " "Of" + " " "Python"
print(challenge)

# concatenate string "Coding", "For", "All"
mission = "Coding" + " " "For" +" " "All"
print(mission)

# declare variable named company and assign value "Coding For All" 
company = "Coding For All"
print(company)

# find the length of the company 
print(len(company))

# change all the characters to uppercase letters
print(company.upper())

# change all the characters to lowercase letters
print(company.lower())

# use capitalize() method 
print(company.capitalize())

# use title() method 
print(company.title())

# use swapcase() method
print(company.swapcase())

# slice out the first word 
print(company[0:6])

# checking coding using find 
print(company.find('Coding'))

# checking coding using index 
print(company.index('Coding'))

# replace coding with Python 
print(company.replace("Coding", "Python"))

# replace for all with for everyone 
message = "Python for Everyone" 
print(message.replace("Python for Everyone", "Python for All"))

# split the string "Coding for All using space as separator" 
print(company.split())

# split the string at the comma 
companies = "Facebook, Google, Oracle, Apple, IBM, Amazon"
print(companies.split(','))

# character index at 0 
print(company[0])

# character index at 10 
print(company[10])

# abbreviation for Python For Everyone 
abbreviation_one = ' Python For Everyone (PFE) '
print(abbreviation_one)

# abbreviation for Coding For All 
abbreviation_two = ' Coding For All (CFA)'
print(abbreviation_two)

# use index to determine the position of C 
print(company.index('C'))

# use index to determine the position of F 
print(company.index('F'))

# use rfind to determine the position of the last occurence
motto = "Coding For All People"
print(motto.rfind('I'))

# use find() method to find the position of first occurence of the word 'because'
disclaimer = "You cannot end a sentence with because because  because is a conjuction" 
print(disclaimer.find('because'))

# use index() method to find the position of first occurence of the word 'because'
print(disclaimer.index('because'))

# use rindex() method to find the position of the last occurrence of the word 'because'
print(disclaimer.rindex('because'))

# slice the word 'because because because' 
print(disclaimer[31:55])

# use startswith() method 
print(company.startswith('Coding'))

# use endswith() method 
print(company.endswith('coding'))

# remove left and right trailling spaces
message = "   Coding For All  "
print(message.strip())

# which variables return True 
message_one = "30DaysOfPython"
print(message_one.isidentifier())
message_two = "thirty_days_of_Python"
print(message_two.isidentifier())

# join list with hash with space string 
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyrammid','Falcon']
result = '# '.join(python_libraries)
print(result)

# use new line escape character to separate sentences 
sentence = "I am enjoying this challenge. \n I just wonder what is next."
print(sentence.strip())

# use tab escape sequence  to write 
print("Name\tAge\tCountry\tCity")
print("Byrone\t30\tKenya\tKisumu")

# use the string formatting method 
radius = 10 
area = 3.14 * radius ** 2 
print(f"The area of a circle with radius {radius} is {int(area)} meters square")

# use string formatting method 
num_one = 8 
num_two = 6 
print(f"{num_one} + {num_two} = {num_one + num_one}")
print(f"{num_one} - {num_two} = {num_one - num_two}")
print(f"{num_one} * {num_two} = {num_one * num_two}")
print(f"{num_one} / {num_two} = {num_one / num_two:.2f}")
print(f"{num_one} // {num_two} = {num_one // num_two}")
print(f"{num_one} ** {num_two} = {num_one ** num_two}")