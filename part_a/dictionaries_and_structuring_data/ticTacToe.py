def printBoard(board):
  print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
  print('-+-+-')
  print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
  print('-+-+-')
  print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def analyzeBoard(board, symbol, location):
  diagMove = False
  locations = location.split('-') #mid-R
  diagonalA = ['top-L', 'mid-M', 'low-R']
  diagonalB = ['low-L', 'mid-M', 'top-R']

  # get all of the keys that contain mid or R
  listKeys = list(board.keys())
  filterKeys = []
  for key in listKeys:
    if ( locations[0] in key or locations[1] in key ):
      filterKeys.append(key)

  # First check:  mid-R, mid-M, mid-L
  count = 0

  for key in filterKeys:
    if ( locations[0] in key and board[key] == symbol ):
      count += 1
    if ( locations[0] in key and board[key] != symbol ):
      break

  if count == 3:
    return True
  else: 
    count = 0
  
  print('First check: failed')

  # Second check:  top-R, mid-R, low-R
  for key in filterKeys:
    if ( locations[1] in key and board[key] == symbol ):
      count += 1
    if ( locations[1] in key and board[key] != symbol ):
      break

  if count == 3:
    return True
  else: 
    count = 0

  print('Second check: failed')

    
  # Check if location is any corner, if so check for diagonal 
  if ( location in diagonalA or location in diagonalB ):
    diagMove = True
  else:
    return False
  
  for key in diagonalA:
    if ( diagMove and board[key] == symbol ):
      count += 1
    if ( diagMove and board[key] != symbol ):
      break
  
  print('After the first diagnoalA check ' + str(count))

  if count == 3:
    return True
  else: 
    count = 0

  for key in diagonalB:
    if ( diagMove and board[key] == symbol ):
      count += 1
    if ( diagMove and board[key] != symbol ):
      break
  
  print('After the first diagnoalB check ' + str(count))

  if count == 3:
    return True
  else:
    count = 0

  return (count == 3) if True else False


theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': '',
            'mid-L': ' ', 'mid-M': 'X', 'mid-R': 'O',
            'low-L': ' ', 'low-M': ' ', 'low-R': 'O'}

turn = 'X'
isWon = False
count = 3

while count < 9:
  printBoard(theBoard)
  print('Turn for ' +  turn + '. Move on which space?')
  move = input()

  if( 'X' in theBoard[move] or 'O' in theBoard[move]):
    print('Space is already occupied. Try again')
    continue
  else:
    theBoard[move] = turn
    count += 1

  if(count > 4):
    isWon = analyzeBoard(theBoard, turn, move)

  if isWon:
    print(turn + ' is the winner of this match!!')
    break

  if turn == 'X':
    turn = 'O'
  else:
    turn = 'X'

printBoard(theBoard)