print("Hello there!\nHow are you?\nI\'m doing fine.")

print(r'That is Carol\'s cat.')

print('''Dear Alice, 

Eve's cat has been arrested for catnapping, cat burglary, and extrotion.
      
Sincerely, 
Bob''')

spam = 'Hello world!'

print(spam[0:5])
print(spam[6:len(spam)-1])
print(spam[6:])

# in and not in 
print('Hell' in spam)

print('How are you?')
feeling = input()
if feeling.lower() == 'great':
  print('I feel great too')
else:
  print('I hope the rest of your day is good')


while True: 
  print('Enter your age:')
  age = input()
  if age.isdecimal():
    break
  print('Please enter a number for your age')

while True:
  print('Select a new password (letters and numbers only)')
  password = input()
  if password.isalnum():
    break
  print('Passwords can only have letters and numbers')


spam.startswith('Hello')
spam.endswith('world!')


x = ', '.join(['cats','rats','bats'])
print(x)


'My name is Simon'.split()

# right-justify 'Hello' in a string of total length 10. 
# 'Hello' is five characters, so five spaces will be added to its left
# giving us a string of 10 characters with Hello jusitfied right
'Hello'.rjust(10)

'Hello'.ljust(10)

'Hello'.rjust(20, '*')
'Hello'.ljust(10, '-')

'Hello'.center(20)
'Hello'.center(20,'=')

spam = '    Hello World     '
spam.strip()
spam.lstrip()
spam.rstrip()


spam.strip('l')
