#At First we Creat the Board :
board = {1: ' ',2: ' ',3: ' ',
         4: ' ',5: ' ',6: ' ',
         7: ' ',8: ' ',9: ' ',}

def printBoard(board):
    print("\n")
    print(board[1]+ '|' +board[2]+ '|' +board[3] )
    print('-+-+-')
    print(board[4]+ '|' +board[5]+ '|' +board[6] )
    print('-+-+-')
    print(board[7]+ '|' +board[8]+ '|' +board[9] )
    print('-+-+-')
    print("\n")
    


#check if the position isn't busy:
def spaceBoard(position):
    if(board[position]== ' '):
        return True
    else:
        return False
#the estimated of wins:    
def checkForWin():
    
  if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
      return True
  elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
      return True
  elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
      return True
  elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
      return True
  elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
      return True
  elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
      return True
  elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
      return True
  elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
      return True
  else:
      return False
    
    
def checkWhichMarkWin(mark):
    
  if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
      return True
  elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
      return True
  elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
      return True
  elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
      return True
  elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
      return True
  elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
      return True
  elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
      return True
  elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
      return True
  else:
      return False

#The condtion of draw:
def checkForDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
        
    return True

def insertLetter(letter, position):
    if spaceBoard(position):
        board[position] = letter
        printBoard(board)
        if (checkForDraw()):
            print("Draw!")
            exit()
        if checkForWin():
            if letter == 'x':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()

        return


    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return
        
player = 'o'
bot = 'x'        

def playerMove():
    print("\n")
    print("enter number opposite to the place of: ")
    print('1'+ '|' +'2'+ '|' +'3' )
    
    print('4'+ '|' +'5' + '|' +'6' )
    
    print('7'+ '|' +'8'+ '|' +'9' )

    try:
        position = int(input("Enter the position For 'O':"))
        insertLetter(player, position)
    except:
        #position = int(input("Enter the position For 'O':"))
        #insertLetter(player, position)
        playerMove()
    return
    
def combMove():
    bestScore = -1000
    bestMove = 0
    
    for key in board.keys():
        if(board[key]== " "):
            board[key] = bot
            score = minimax(board, False)
            board[key] = ' '
            if(score > bestScore):
                bestScore = score
                bestMove = key
    insertLetter(bot,bestMove)
    return

def minimax(board, isMaximizing):
    if checkWhichMarkWin(bot):
        return 1000
    elif checkWhichMarkWin(player):
        return -1000
    elif checkForDraw():
        return 0
    
    if isMaximizing:
        bestScore = -1000
            
        for key in board.keys():
            if(board[key]== " "):
                board[key] = bot
                score = minimax(board, False)
                board[key] = ' '
                if(score > bestScore):
                    bestScore = score
                    
        return bestScore
    else:
        bestScore = 800
            
        for key in board.keys():
            if(board[key]== " "):
                board[key] = player
                score = minimax(board, True)
                board[key] = ' '
                if(score < bestScore):
                    bestScore = score
        
        return bestScore
        
    

while not checkForWin():
    
    combMove()
    playerMove()
   
    
    
    #problems:
    #the code enter isertLetter two times so it prints the board two times
