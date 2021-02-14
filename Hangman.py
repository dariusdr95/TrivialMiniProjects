import random

words=["hello","cheese","handle","super","destiny","diamond",\
       "ending","festival","courtesy","perseverance", "humility",\
       "loading","platinum","stupify","donkey","crossroads"]

word = words[random.randint(0,len(words)-1)]
wordList=[]
for i in word:
    if i not in wordList:
        wordList.append(i)
###print(wordList)

livesRemaining=10
correctGuesses=[]
incorrectGuesses=[]

def checkWin():
    global gameOver
    if len(correctGuesses) == len(wordList):
        gameOver = True
        print("You win")

    if livesRemaining==0:
        gameOver = True
        print("You lose")

def wordPrint():
    for i in word:
        if i in correctGuesses:
            print(i, end=" ")
        else:
            print("*", end=" ")
    print("")
gameOver=False

####print(word)
wordPrint()

while gameOver==False:
    guess = input("Enter a letter: ").lower()
    if guess in wordList and gameOver==False:
        correctGuesses.append(guess)
        print(guess, "is a letter!")
        wordPrint()
        checkWin()

    else:
        livesRemaining-=1
        print(guess, "is not a letter!", livesRemaining, "lives remaining")
        wordPrint()
        checkWin()



