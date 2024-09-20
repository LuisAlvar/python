# Dictionaries vs. Lists
spam = ['cats','dogs','moose']
bacon = ['dogs','moose','cats']
print(str(spam == bacon))

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(str(eggs == ham))


# The keys()., values(), and items() method
spam = {'color':'red', 'age': 42}

for k in spam.keys():
  print(k)

for v in spam.values():
  print(v)

for v in spam.items():
  print(list(v))

for k,v in spam.items():
  print('Key: ' + k + ' Value: ' + str(v))

# Checking Whether a Key or Value Exists in a Dictionary 

spam = {'name': 'Zophie', 'age': 7 }

'Zophie' in spam.values()
'color' not in spam.keys()


# The get() method 
picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')


# the setdefault() method 
spam = {'name': 'Pooka', 'age': 5 }
print(spam)
spam.setdefault('color', 'black')
print(spam)


import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0) # ensure that the letter in a key within the dictionary and the count start at zero
    count[character] = count[character] + 1

# in this cause you will have lowercase and uppercase classified independently, includes spacings and gammer marks. 
pprint.pprint(count)
