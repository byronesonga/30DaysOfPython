# sets 
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amzon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 24, 26, 24, 25, 24]

# length of set it_companies 
print(len(it_companies))

# add 'Twitter' to it_companies 
it_companies.add("Twitter")
print(it_companies)

# add multiple IT companies at once 
more_it_companies = ("Snapchat", "YouTube", "Google", "Yahoo")
it_companies.update(more_it_companies)
print(it_companies)

# remove one of the companies 
it_companies.remove("Snapchat")
it_companies.discard("Snapchat")
print(it_companies) 

# remove() method raises an error if an item is not found from the set
# discard() method does not raise an error if  an item is not found from the set 

# join A and B 
C= A.union(B)
print(C) 

# intersection 
print(A.intersection(B))

# subset sets
print(A.issubset(B))

# disjoint sets 
print(A.isdisjoint(B))

# join a with b 
AB = A.union(B) 
print(AB) 

# join B with A 
BA = A.union(B)
print(BA) 

# symmetric difference between A and B 
print(A.symmetric_difference(B))

# delete  both sets 
del A 
del B 

# convert list to a set 
age_set = set(age)
print(age_set) 

# compare length og set and list 
print(len(age))
print(len(age_set))
# length of list is bigger than the length of set(8 for list and 5 for set)

# Data Types
# string:characters enclosed by quotes
# list:collection of items which are ordered, mutable, allow duplicate values, represented by []
# tuple:collection of items which are ordered, immutable, allows duplicate values, represented by ()
# set: collection of items which are unordered, immutable, new items can be added, duplicate members not allowed, represnred by {}
# dictionary: collection of items which are unorderd, mutable, indexed, no duplicate members, represented by {}

# find unique words in the sentence below 
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print(unique_words)