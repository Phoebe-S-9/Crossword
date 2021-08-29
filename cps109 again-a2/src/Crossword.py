'''
Phoebe S.
Cps 109- 12
Assignment 2: cross word puzzle
Nov 15- 25, 2019

Credit to Jenny Long for helping with checking/adding a word horizontally.
Credit to professor Eric Harley's notes for helping with adding the first word and checking/adding a word vertically.
'''

def printBoard(board):
    
    '''
    Displays the board with a border.

    input: a matrix making the board 20 x 20
    ouput: a boader: top and bottom lines are '01234567890123456789'. The second and second last line are underscores.
    A '|' is printed before and after the 20 letters of each row. At the end of each row is printed the index of the row.
    '''
    
    B = len(board)

    for lines in range(5):
        for i in range(B): #rows

            if lines == 0 or lines == 4: #numbers at first and last rows
                if i == 0:
                    print(' ', end = '')

                if i < 10:
                    print(i, end = '')
                else: # ones digit only
                    print(i - 10, end = '')

            elif lines == 1 or lines == 3: # _ at second and second last rows
                if i == 0:
                    print(' ', end = '')
                print('_', end = '')

            else: #main board
                print('|', end = '') 
                for j in range(len(board[i])): #columns
                    print(board[i][j], end = '')
                print('|' + str(i)) #num on side

        print()#new line

#------------
def addFirstWord(board, word): #Q2    

    ''' 2.
    Puts the first word in the middle (vertically and horizontally) of the blank 20x20 board.
    input: the board matrix and the first valid word in the list.
    ouput: True if the word can be added. False otherwise.
    '''
    
    W, B = len(word), len(board)
    validFirstWord = True
    middleColumn = B//2

    if W > B: # invalid first word # too long for the board
        validFirstWord = False
        print('reaches outside grid')
        return validFirstWord

    else: # place first word 
        for column in range(W): 
            middleRow = column + (middleColumn - W//2)
            board[middleColumn][middleRow] = word[column]
        return validFirstWord

#------------
def checkVertical(board, word, row, col): #Q3

    '''3.
    Checks if placing a word is restricted. Invalid words: don't fit on the board, don't intersect with non-blank letters on the board, or change non blank letters on the board.
    Can't over lap a word either.
    input: the current row and column in the board.
    ouput: True if the word can be added to the board (starting at position board[row][col] and going down).
    '''
    #True/False, 1,2,3 = matches, no match, illegal/overlap, outside grid

    W, B = len(word), len(board)
    blank = ' '
    matchingLetter = False

    if W == 1:# word cant be too short
        return 2
    if W> 20:# word cant be too long- starting
        return 3
    
    if W > B - row: # word cant be too long -current
        return matchingLetter

    for char in range(W): #match word letter against board letter  # check if letter match. or if blank: skip 
        boardChar = board[row +char][col] # checks board's row and colums (down ward)#colum is same, and row changes
        wordChar = word[char]
        
        if boardChar == wordChar and board[row + W][col] == blank: #if letters same and not overlapping, then have a match 

            if board[row +char-1][col] != blank: #above
                return 2

            for char in range(W):
                boardCharCheck = board[row +char][col] # checks board's row and colums (down ward)#colum is same, and row changes
                wordCharCheck = word[char]
        
                if boardCharCheck != wordCharCheck:
                    if board[row +char][col -1]!= blank or board[row +char][col +1]!= blank:#L/R
                        return 2

            if board[row  + char+ 1][col] != blank:#below
                return 2

            matchingLetter = True
            return matchingLetter
            
        elif boardChar != wordChar and boardChar!= blank:
            matchingLetter = False
            return matchingLetter # word can't go on board

    return matchingLetter
 

#------------
def addVertical(board, word): #Q4

    '''4.
    Adds a word vertically to the board. The restrictions are checked in checkvertical(board, word, row, col).
    input: the board matrix and a word in the list.
    output: True if it added the word, and False otherwise.
    '''
    
    W, B = len(word), len(board)

    for row in range(B): # across
        for col in range(B):#down #check over the whole board if word can be placed

            output =  checkVertical(board,word, row,col)

            if output == 2:
                print('illegal adjacencies')
                return False
            if output == 3:
                print('reaches outside grid')
                return False

            
            if output:
                for char in range(W): # put word onto the board at that spot
                    board[row + char][col] = word[char] 
                return True #if added 

    print('no matching letter')
    return False

#------------
def checkHorizontal(board, word, row, col): 
    
    '''
    Checks if placing a word is restricted. Invalid words: don't fit on the board, don't intersect with non-blank letters on the board, or change non blank letters on the board. or overlaps
    input: the current row and column in the board.
    ouput: True if the word can be added to the board (starting at position board[row][col] and going right).
    '''
     
    W, B = len(word), len(board)
    blank = ' '
    matchingLetter = False

    if W == 1:# word cant be too short
        return 2
    
    if W> 20:# word cant be too long - start
        return 3
    
    if W > B - row: # word cant be too long- current
        return matchingLetter

    for char in range(W): #match word letter against board letter  # check if letter match. or if blank: skip 
        boardChar = board[col][row+char] # checks board's row and colums (towards right)#row is same, and col changes
        wordChar = word[char]
        
        if boardChar == wordChar and board[col][row + W] == blank: #if letters same and not overlapping, then have a match 

            if board[col][row+char-1] != blank:  #left # illegal
                return 2

            for char in range(W):
                boardCharCheck = boardChar = board[col][row+char] 
                wordCharCheck = word[char]
            
                if boardCharCheck != wordCharCheck:
                     if board[col -1][row+char] != blank or board[col+1][row+char] != blank:#a/b #illegal
                         return 2
                
            if board[col][row+char+1]  != blank:#Right #illegal
                return 2
            
            matchingLetter = True
            return matchingLetter
            
        elif boardChar != wordChar and boardChar!= blank:
            matchingLetter = False
            return matchingLetter # word can't go on board

    return matchingLetter
 
#------------
def addHorizontal(board, word):

    '''
    Adds a word horizontally to the board. The restrictions are checked in checkHorizontal(board, word, row, col).
    input: the board matrix and a word in the list.
    output: True if it added the word, and False otherwise.
    '''
  
    W, B = len(word), len(board)

    for row in range(B): # across
        for col in range(B):#down #check over the whole board if word can be placed

            output =  checkHorizontal(board, word, row,col)

            if output == 2:
                print('illegal adjacencies')
                return False
            if output == 3:
                print('reaches outside grid')
                return False
     
            if output: 
                for char in range(W): # put word onto the board at that spot
                     board[col][row + char] = word[char] 
                return True #if added 

    print('no matching letter')
    return False    
   
#------------------MAIN 
def crossword(L): 
    
    '''
    Uses the helper functions to add a list (L) of words to the board.
    Starts with the first valid word in the middle and alternates between vertical and horizontal placements.

    input: a list of strings (L), and a matrix creating a board.
    output: a cross word using all of the acceptable words in the list. As well as the outcomes of each functions.
    '''
    blank = ' ' 
    board = [[ blank ] * 20 for i in range(20) ]
    firstWordPlaced = False
    wordCounter = 0
    word = L[wordCounter]
    
    W, B = len(word), len(board)
    row, col = 0,0

    print('The list of words(L) is:', L)
                
    for wordCounter in range(len(L)): # place every letter in the list

        word = L[wordCounter]
        print('\nTrying to add the word:', word)
        
        if firstWordPlaced == False:
            fWord = addFirstWord(board, word)
            #print('First word works:', fWord) # outputs true or false # q2 
            
            if fWord:
                firstWordPlaced = True
            
        elif wordCounter % 2 == 0: #is even #try hoirz #if not, try vert
            outputH = addHorizontal(board, word)
            print('addHorizontal:',outputH)
            
            if outputH == False:
                outputV = addVertical(board, word)
                print('addVertical:', outputV) 
                   
        else:  #is odd #try vert #if not, try horiz
            outputV = addVertical(board, word)
            print('addVertical:', outputV) 
            
            if outputV == False:
                outputH = addHorizontal(board, word) 
                print('addHorizontal:', outputH) 
            
        print() # new line
    printBoard(board) # final
    print()

#main
L = ['hippopotamus', 'horse',  'loon', 'snake', 'cat', 'dinosaur','b', 'jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj','a', 'xx'] 
crossword(L)

L = ['Hippopotomonstrosesquippedaliophobia', 'rattlesnake', 'hhhhhhhhhhhhhhhhhhhhh',  'top', 'snake', 'noodles', 'hippopotamus', 'hello', 'jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj', 'soccer','greetings', 'surname',  'jail', 'fire', 'cat', 'firetruck', 'blackcat', 'smile', 'naked', 'star', 'sun', 'toilet', 'great', 'greedy', 'dark', 'marrow', 'spoiled', 'light', 'darker', 'near', 'on', 'a', 'arrow', 'wars'] 
crossword(L)



