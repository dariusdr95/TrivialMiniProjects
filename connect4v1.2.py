import random

"""For some reason, whenever the game is over, the 
win is reported and the board is repeated several times
the numbers vary and I can't see a pattern to this.

I also had a problem with checking wins on the diagonals.
This appears to be fixed but I have not tested it extensively"""

row7 = ["7", "_", "_", "_", "_", "_", "_", "_"]
row6 = ["6", "_", "_", "_", "_", "_", "_", "_"]
row5 = ["5", "_", "_", "_", "_", "_", "_", "_"]
row4 = ["4", "_", "_", "_", "_", "_", "_", "_"]
row3 = ["3", "_", "_", "_", "_", "_", "_", "_"]
row2 = ["2", "_", "_", "_", "_", "_", "_", "_"]
row1 = ["1", "_", "_", "_", "_", "_", "_", "_"]
Xaxis = [" ", "1", "2", "3", "4", "5", "6", "7"]
Board = [row7, row6, row5, row4, row3, row2, row1, Xaxis]
print(*Board, sep="\n")



def winConditions():
    global gameOver
    if c1 == "R" and c2 == "R" and c3 == "R" and c4 == "R":
        print("You win!")
        gameOver = True
        print(*Board, sep="\n")


    elif c1 == "B" and c2 == "B" and c3 == "B" and c4 == "B":
        print("You Lose!")
        gameOver = True
        print(*Board, sep="\n")


gameOver = False
####Entering the player's move

"""The code below attempts to drop the counter into 
the lowest row. However, if this row is already occupied
it attempts the row above.  If all the rows have been tried
the column is reported as full and the player is told to
select a new column"""

while gameOver == False:
    move = int(input("Select a column: "))
    if move > 7:
        move = int(input("Not a column. Select a new column: "))
    entered = False
    i = 7
    while entered == False and gameOver == False:
        if i < 0:  ### In case the column is full
            move = int(input("That column is full. Select a column: "))
            entered = False
            i = 7
        elif Board[i][move] == "_": ###Testing row. Inputting if available
            Board[i][move] = "R"
            entered = True
        else:  ###Iterating
            i -= 1
        ###Entering the opponents move
        Oppmove = random.randint(1, 7)
        Oppentered = False
        i2 = 7
    while Oppentered == False and gameOver == False:
        if i2 < 0:
            Oppmove = random.randint(1, 7)
            Oppentered = False
            i2 = 7
        elif Board[i2][Oppmove] == "_":
            Board[i2][Oppmove] = "B"
            i2 = 7
            Oppentered = True

        else:
            i2 -= 1
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0

        ###Checking vertical wins
        for col in range(1, 7):
            for row in range(0, 4):
                c1 = Board[row][col]
                c2 = Board[row + 1][col]
                c3 = Board[row + 2][col]
                c4 = Board[row + 3][col]
                ###print(c1,c2,c3,c4)
                winConditions()

            ###Checking horizontal wins

            for col in range(1, 5):
                for row in range(0, 7):
                    c1 = Board[row][col]
                    c2 = Board[row][col + 1]
                    c3 = Board[row][col + 2]
                    c4 = Board[row][col + 3]
                    winConditions()

            ###Checking Right/Down wins
            for col in range(1, 4):
                for row in range(0, 4):
                    c1 = Board[row][col]
                    c2 = Board[row + 1][col + 1]
                    c3 = Board[row + 2][col + 2]
                    c4 = Board[row + 3][col + 3]
                    winConditions()

            ###Checking Right/Up wins
            for col in range(1, 4):
                for row in range(3, 7):
                    c1 = Board[row][col]
                    c2 = Board[row - 1][col + 1]
                    c3 = Board[row - 2][col + 2]
                    c4 = Board[row - 3][col + 3]
                    winConditions()

    ###Final Print
    if gameOver == False:
        print(*Board, sep="\n")