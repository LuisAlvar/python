def printPicnic(itemsDict, leftWidth, rightWidth):
  print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
  for k, v in itemsDict.items():
    print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)

#ljust you push the content to the left by adding delimiters, if any, on the right.
#rjust you push the content to the right by add delimiters, if any, on the left.
printPicnic(picnicItems, 20, 6)


