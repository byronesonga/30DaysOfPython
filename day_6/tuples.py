# empty tuple 
empty_tuple = ()
print(empty_tuple)  

# my brothers 
brothers = ("Owen", "Oketch", "Sparrow", "Songa") 
# my sisters 
sisters = ("Violet", "Sofia", "Christine", "Mary", "Lucy") 

# join tuple
siblings = brothers + sisters 
print(siblings) 

# length of tuple 
print(len(siblings))

# modify tuple 
family_members = list(siblings)
family_members.append("Songa")
family_members.append("Rose")
family_members = tuple(family_members)
print(family_members) 

# unpacking tuples 
ow, ok, sp, so, vi, sf, ch, ma, lu,*pa = family_members
print(ow)
print(ok)
print(sp)
print(so)
print(vi)
print(sf)
print(ch)
print(ma)
print(lu)
print(pa)

# fruits tuple 
fruits = ("mango", "apple", "orange", "lemon") 
# vegetables tuple 
vegetables = ("kales", "spinach", "cabbage", "tomatoes")
# animal_products tuple
animal_products = ("eggs", "meat", "milk", "blood") 

# joining tuples 
food_stuff_tp = fruits + vegetables + animal_products 
print(food_stuff_tp)

# changing tuple to list 
food_stuff_lt = list(food_stuff_tp) 
print(food_stuff_lt)

# slice out middle item  in list 
middle_index = len(food_stuff_lt) // 2
middle_item = food_stuff_lt[middle_index]
print(middle_item)

# slice out middle item in tuple 
middle_tuple_index = len(food_stuff_tp) // 2 
middle_item_tuple = food_stuff_tp[middle_tuple_index]
print(middle_item_tuple) 

# slice out first three items from food_staff_lt list
print(food_stuff_lt[0:3])

# slice out last three items from food_staff_lt list
print(food_stuff_lt[9:])

# check if an item exists in tuple 
print("orange" in food_stuff_tp) 

# delete tuple 
del food_stuff_tp 

# nordic countries 
nordic_countries = ('Denmark', 'Finland', 'Norway', 'Iceland') 
print('Estonia' in nordic_countries) 
print('Finland' in nordic_countries)
