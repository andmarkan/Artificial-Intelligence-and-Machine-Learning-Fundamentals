# The first 65 lines contain the code of Activity 02
# This activity's code follows after line 66

from random import choice 

ComboIndices = [ 
    [0,1,2], 
    [3,4,5], 
    [6,7,8], 
    [0,3,6], 
    [1,4,7], 
    [2,5,8], 
    [0,4,8], 
    [2,4,6] 
]

EMPTY_SIGN = '.' 
AI_SIGN = 'X' 
OPPONENT_SIGN = 'O'

def printBoard( Board ): 
    print( " " ) 
    print( ' '.join( Board[:3] ) ) 
    print( ' '.join( Board[3:6] ) ) 
    print( ' '.join( Board[6:] ) ) 
    print( " " )

def opponentMove( Board, row, column ): 
    index = 3 * ( row - 1 ) + (column - 1) 
    if Board[index] == EMPTY_SIGN: 
        return Board[:index] + OPPONENT_SIGN + Board[index+1:] 
    return Board

def allMovesFromBoard( Board, sign ): 
    moveList = [] 
    for i, v in enumerate( Board ): 
        if v == EMPTY_SIGN: 
            moveList.append( Board[:i] + sign + Board[i+1:] ) 
    return moveList 

def aiMove( Board ): 
    return choice( allMovesFromBoard( Board, AI_SIGN ) )

def gameWonBy( Board ): 
    for index in ComboIndices: 
        if Board[ index[0] ] == Board[ index[1] ] == Board[ index[2] ] != EMPTY_SIGN: 
            return Board[ index[0] ] 
    return EMPTY_SIGN

def gameLoop():  
    Board = EMPTY_SIGN * 9 
    emptyCellCount = 9 
    isGameEnded = False 
    while emptyCellCount > 0 and not isGameEnded: 
        if emptyCellCount % 2 == 1: 
            Board = aiMove( Board ) 
        else: 
            row = int(input('Enter row: ')) 
            col = int(input('Enter column: ')) 
            Board = opponentMove( Board, row, col ) 
        printBoard( Board ) 
        isGameEnded = gameWonBy( Board ) != EMPTY_SIGN 
        emptyCellCount = sum( 1 for cell in Board if cell == EMPTY_SIGN ) 
    print( 'Game has been ended.' )

#----------Activity 03---------------

def allMovesFromBoardList( BoardList, sign ): 
    moveList = [] 
    for Board in BoardList: 
        moveList.extend( allMovesFromBoard( Board, sign ) ) 
    return moveList

def filterWins( moveList, aiWins, opponentWins ): 
    for Board in moveList: 
        wonBy = gameWonBy( Board ) 
        if wonBy == AI_SIGN: 
            aiWins.append( Board ) 
            moveList.remove( Board ) 
        elif wonBy == OPPONENT_SIGN: 
            opponentWins.append( Board ) 
            moveList.remove( Board )

def countPossibilities(): 
    Board = EMPTY_SIGN * 9 
    moveList = [Board] 
    aiWins = [] 
    opponentWins = [] 
    for i in range(9): 
        print( 'step ' + str( i ) + '. Moves: ' + str(len( moveList))) 
        sign = AI_SIGN if i%2 == 0 else OPPONENT_SIGN 
        moveList = allMovesFromBoardList( moveList, sign ) 
        filterWins( moveList, aiWins, opponentWins ) 
    print( 'First player wins: ' + str( len( aiWins ) ) ) 
    print( 'Second player wins: ' + str( len( opponentWins ) ) ) 
    print( 'Draw', str( len( moveList ) ) ) 
    print( 'Total', str( len( aiWins ) + len( opponentWins ) + len( moveList ) ) )