import os
import json

square = [*'0123456789']

def checkForWin():
    returnValue = 0
    if square[1]==square[2]==square[3]: returnValue = 1
    elif square[4]==square[5]==square[6]: returnValue = 1
    elif square[7]==square[8]==square[8]: returnValue = 1
    elif square[1]==square[4]==square[7]: returnValue = 1
    elif square[2]==square[5]==square[8]: returnValue = 1
    elif square[3]==square[6]==square[9]: returnValue = 1
    elif square[1]==square[5]==square[9]: returnValue = 1
    elif square[3]==square[5]==square[7]: returnValue = 1
    elif (square[1]!='1' and square[2]!='2' and square[3]!='3' and square[4]!='4' 
          and square[5]!='5' and square[6]!='6' and square[7]!='7' and square[8]!='8' 
          and square[9]!='9'): 
        returnValue = 0
    else: returnValue = -1
    return returnValue

def displayBoard():
    os.system('cls')
    print(f"""
    \n\n\tTic Tac Toe\n\n
    Player 1 (X)  -  Player 2 (O)\n\n\n
         |      |       \n
      {square[1]}  |  {square[2]}   |  {square[3]}  \n
    _____|______|_______\n
         |      |       \n
       {square[4]} |  {square[5]}   |  {square[6]}  \n
    _____|______|_______\n
         |      |       \n
       {square[7]} |  {square[8]}   |  {square[9]}  \n
         |      |       \n\n    
        """)
    
def markBoard(mark):
    global moves
    global player
    if choice==1 and square[1]=='1': 
        square[1] = mark
        moves['1']=str(player)+"chosen."
    elif choice==2 and square[2]=='2': 
        square[2] = mark
        moves['2']=str(player)+"chosen."
    elif choice==3 and square[3]=='3': 
        square[3] = mark
        moves['3']=str(player)+"chosen."
    elif choice==4 and square[4]=='4': 
        square[4] = mark
        moves['4']=str(player)+"chosen."
    elif choice==5 and square[5]=='5': 
        square[5] = mark
        moves['5']=str(player)+"chosen."
    elif choice==6 and square[6]=='6': 
        square[6] = mark
        moves['6']=str(player)+"chosen."
    elif choice==7 and square[7]=='7': 
        square[7] = mark
        moves['7']=str(player)+"chosen."
    elif choice==8 and square[8]=='8': 
        square[8] = mark
        moves['8']=str(player)+"chosen."
    elif choice==9 and square[9]=='9': 
        square[9] = mark
        moves['9']=str(player)+"chosen."
    else:
        print("Invalid move ")       
        player -= 1

if __name__ == "__main__":
    player = 1
    moves = {}
    while True:
        displayBoard()
        player = 1 if player%2 else 2
        choice = int(input(f"Player {player}, enter a number: "))
        mark = 'X' if player == 1 else 'O'
        markBoard(mark)
        gameStatus = checkForWin()
        player += 1
        if gameStatus != -1: break
    if gameStatus == 1: print(f"Player {player - 1} win")
    else: print("Game draw")
    print(moves)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(moves, f, ensure_ascii=False, indent=4)

