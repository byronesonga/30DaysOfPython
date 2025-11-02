# empty list 
fruits = []

# list with items 
fruits = ['mango', 'lemon','apple','orange','banana','lime']

# length of the list 
print(len(fruits))

# get first item 
first_fruit = fruits[0]
print(first_fruit)

# middle item 
middle_index = len(fruits) // 2 
middle_fruit = fruits[middle_index]
print(middle_fruit)

# last item 
last_index = len(fruits) - 1  
last_fruit = fruits[last_index]
print(last_fruit)

# mixed data types in a list 
mixed_data_types = [{'name':'Byrone Songa', 'age':30, 'height':4.5, 'marital_status':False, 'address':'kisumu'}]
print(mixed_data_types)

# declare  list variable and assign values 
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# print the list of the companies 
print(it_companies)

# the number of the companies 
print(len(it_companies))

# first company 
first_company =  it_companies[0]
print(first_company)

# middle company 
middle_index = len(it_companies) // 2 
middle_company = it_companies[middle_index]
print(middle_company)

# last company 
last_index = len(it_companies) - 1 
last_company = it_companies[last_index]
print(last_company)

# modify an it_company 
it_companies[0] = "Lenovo"
print(it_companies)

# add an it_company 
it_companies.append("Sony")
print(it_companies)

# insert an it company 
it_companies.insert(middle_index, "Hp")
print(it_companies)

# change to uppercase 
it_companies[0] = it_companies[0].upper()
print(it_companies)

# join the it_companies using # 
result = '# '.join(it_companies)
print(result)

# check if a certain company exists  in the it_company list 
print('Amazon' in it_companies)

# sort the list using sort() method
it_companies.sort()
print(it_companies)

# reverse the list in desceding order 
it_companies.reverse() 
print(it_companies)

# slice the first 3 it_companies 
print(it_companies[0:3])

# slice the last 3 it_companies 
print(it_companies[6:9])

# slice the middle it_company 
print(it_companies[middle_index])

# remove the first it_company 
print(it_companies.pop(0))

# remove the middle it_company 
print(it_companies.pop(middle_index))

# remove the last it_company 
print(it_companies.pop(last_index))

# remove all the it_companies 
it_companies.clear()
print(it_companies)

# destroy the it_companies 
del it_companies 

# joining lists 
front_end = ['HTML', 'CSS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_result = front_end + back_end
print(joined_result)

# copy list 
full_stack = joined_result.copy()
print(full_stack)

# insert item in a list 
full_stack.insert(4, "SQL")
full_stack.insert(4, "Python")
print(full_stack)

# list of students ages 
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# sort ages 
ages.sort() 
print(ages)

# min age 
print(min(ages)) 

# max age 
print(max(ages))

# midian age 
middle_index = len(ages) // 2 
midian_age = ages[middle_index] 
print(midian_age)

# average age 
number_of_students = len(ages) 
total_age = sum(ages)
average_age = total_age // number_of_students
print(average_age)

# range of ages 
print(max(ages) - min(ages))

# comparing values 
difference_one = abs(max(ages) - average_age)
print(difference_one)

# comparing values 
difference_two = abs(min(ages) - average_age)
print(difference_two)

# countries list 
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

# middle country 
middle_country_index = len(countries) // 2 
middle_country = countries[middle_country_index]
print(middle_country) 

# divide the countries into two 
first_country = countries[:middle_country_index]
second_country = countries[middle_country_index:]
print(first_country)
print(second_country) 

# unpack country lists 
ch, ru, us, *scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(ch)
print(ru)
print(us)
print(scandic)