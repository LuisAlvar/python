#! python3
# tablePrinter.py - Display it in a well-organized table with each column right-justified. 
# Assume that all the inner lists will contain the same number of strings.

tableData = [
  ['apples', 'oranges', 'cherries', 'banana'],
  ['Alice', 'Bod', 'Carol','David'],
  ['dogs','cats','moose','goose']
]

def printTable(Data):
  numOfLists = len(Data)
  indexOnList = 0
  maxLenthItem = 0
  itemsPerList = []
  while numOfLists > indexOnList:
    for value in Data[indexOnList]:
        if(len(value) > maxLenthItem):
           maxLenthItem = len(value)
    itemsPerList.append(len(Data[indexOnList]))
    indexOnList += 1
  
  print('max length character: ' + str(maxLenthItem))
  print(itemsPerList)
  
  indexOnList = 0
  accStr = ""

  for j in range(0, 4, 1):
    for i in range(0, len(Data), 1):
      accStr += Data[i][j].rjust(maxLenthItem)
    accStr += "\n"

  print(accStr)

printTable(tableData)