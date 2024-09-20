def totalBrought(guests, item):
  numBrought = 0
  for k, v in guests.items():
    numBrought = numBrought + v.get(item,0)
  return numBrought

allGuest = {'Alice': {'apples': 5, 'pretzels': 12},
            'Bob': {'ham sandwiches': 3, 'apples': 2},
            'Carol': {'cups': 3, 'apple pies': 1}
            }


print('Number of things being brought: ')
print(' - Apples ' + str(totalBrought(allGuest, 'apples')))
print(' - Apples ' + str(totalBrought(allGuest, 'apples')))
print(' - Apples ' + str(totalBrought(allGuest, 'apples')))
print(' - Apples ' + str(totalBrought(allGuest, 'apples')))
print(' - Apples ' + str(totalBrought(allGuest, 'apples')))