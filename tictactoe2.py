import random

row1 = ["_","_","_"]
row2 = ["_","_","_"]
row3 = ["_","_","_"]

grid = [row1,row2,row3]

print("You are Xs",*grid, sep ="\n")
game_over=False

while game_over==False:

    #Player selection
    xcoordinate = int(input("enter an x coordinate "))-1
    ycoordinate = 3-int(input("enter a y coordinate "))
    if grid[ycoordinate][xcoordinate] == "x" or grid[ycoordinate][xcoordinate] == "o":
        print("Already taken")
        xcoordinate = int(input("enter an x coordinate "))-1
        ycoordinate = 3-int(input("enter a y coordinate "))
    else:
        grid[ycoordinate][xcoordinate] = "x"

        #Opponent selection
        xcoordinate2 = random.randint(1,3)-1
        ycoordinate2 = 3-random.randint(1,3)
        while (grid[ycoordinate2][xcoordinate2]) == "x" or (grid[ycoordinate2][xcoordinate2])=="o":
            xcoordinate2 = random.randint(1, 3) - 1
            ycoordinate2 = 3 - random.randint(1, 3)
        (grid[ycoordinate2][xcoordinate2]) = "o"

        ###Win conditions
        if grid[0][0] == "x" and grid[0][1] == "x" and grid[0][2] == "x" or \
                grid[1][0] == "x" and grid[1][1] == "x" and grid[1][2] == "x" or \
                grid[2][0] == "x" and grid[2][1] == "x" and grid[2][2] == "x" or \
                grid[0][0] == "x" and grid[1][0] == "x" and grid[2][0] == "x" or \
                grid[0][1] == "x" and grid[1][1] == "x" and grid[2][1] == "x" or \
                grid[0][2] == "x" and grid[1][2] == "x" and grid[2][2] == "x" or \
                grid[0][0] == "x" and grid[1][1] == "x" and grid[2][2] == "x" or \
                grid[0][2] == "x" and grid[1][1] == "x" and grid[2][0] == "x":
            print(grid)
            print("You win :)")
            game_over = True
        elif grid[0][0] == "o" and grid[0][1] == "o" and grid[0][2] == "o" or \
                grid[1][0] == "o" and grid[1][1] == "o" and grid[1][2] == "o" or \
                grid[2][0] == "o" and grid[2][1] == "o" and grid[2][2] == "o" or \
                grid[0][0] == "o" and grid[1][0] == "o" and grid[2][0] == "o" or \
                grid[0][1] == "o" and grid[1][1] == "o" and grid[2][1] == "o" or \
                grid[0][2] == "o" and grid[1][2] == "o" and grid[2][2] == "o" or \
                grid[0][0] == "o" and grid[1][1] == "o" and grid[2][2] == "o" or \
                grid[0][2] == "o" and grid[1][1] == "o" and grid[2][0] == "o":
            print(grid)
            print("You lose :(")
            game_over = True

    print(*grid, sep ="\n")


