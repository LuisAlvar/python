3# the collatz sequence 
def collatz(number):
  if (number % 2 == 0):
    print('number is even')
    response = number // 2
    print('return -- > value :: ' + str(response))
    return response
  
  elif (number % 2 == 1):
    print('number is odd')
    response = 3 * number + 1
    print('return --> value :: ' + str(response))
    return 3 * number + 1

print('Please enter a number: ', end='')
try:
  num = input()
  initial = int(num)
except ValueError:
  print('Custom Message ::: You must enter an integer')

while True:
  value = collatz(initial)
  if (value == 1):
    break
  else:
    initial = value



