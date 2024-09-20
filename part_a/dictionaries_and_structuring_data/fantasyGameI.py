def displayInventory(invent):
  print("Inventory:")
  sumOfItems = 0
  for k, v in invent.items(): # better version
    print(str(v) + ' ' + k)
    sumOfItems += v
  print("Total number of items: " + str(sumOfItems))
  # sumOfItems = 0
  # listOfItems = invent.keys()
  # for item in listOfItems:
  #   sumOfItems += invent[item]
  #   print(str(invent[item]) + " " + str(item))
  # print("Total number of items: " + str(sumOfItems))


# def displayInventory2(invent):
#   print("Inventory:")
#   sumOfItems = 0
#   for k, v in invent.items(): # better version
#     print(str(v) + ' ' + k)
#     sumOfItems += v
#   print("Total number of items: " + str(sumOfItems))

def addToInventory(invent, addedItems):
  for aNewItem  in addedItems:
    if (aNewItem in invent.keys()):
      invent[aNewItem] = invent[aNewItem] + 1
    else:
      invent.setdefault(aNewItem, 1)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(inv, dragonLoot)
displayInventory(inv)


