import sys
from operator import indexOf
import urllib.request
from urllib.request import Request, urlopen
import random

#Read File from github
wordListURL = "https://raw.githubusercontent.com/charlesreid1/five-letter-words/master/sgb-words.txt"
reqWord = Request(wordListURL, headers={'User-Agent': 'Mozilla/5.0'})

web_file = urlopen(reqWord).read()

gitFile = web_file.decode('utf-8')
#Getting random word
l = random.sample(gitFile.split("\n"), 1)#Random word stored in list l
randomWord = str(l[0]) #storing word from list to string

allInputs = []  #list to store all user inputs

#Initial Function to print rules
def rules():
    print("\033[1;30;47mRULES TO PLAY: ", end="")
    clearColor()
    print("\nGuess the WORDLE in six tries.")
    print("Each guess must be a valid five-letter word. Hit the enter button to submit.")
    print("After each guess, the color of the tiles will change to show how close your guess was to the word.")
    print("-"*50)
    bold("Examples")
    setGreen("W")
    bold("E A R Y")
    print("The letter W is in the word and in the correct spot.\n")
    print("\033[1mP ", end = "")
    setYellow("I")
    bold("L L S")
    print("The letter I is in the word but in the wrong spot.\n")
    print("\033[1mV A G ", end = "")
    setGray("U")
    bold("E")
    print("The letter U is not in the word in any spot.")
    print("-"*50)   
    print("Type help or ? to open rule book") 
    print("Type history or * to display all last moves") 

#Functions to set color and style
def setGray(i):
    print("\033[1;37;40m", end=" ")
    print(i.upper(), end=" ")

def setYellow(i):
    print("\033[1;37;43m", end=" ")
    print(i.upper(), end=" ")

def setGreen(i):
    print("\033[1;37;42m", end=" ")
    print(i.upper(), end=" ")

def clearColor():
    print("\033[0;37;48m")

def bold(i):
    print("\033[0m\033[1m", i, "\033[0m\n")

def boldGreen(i):
    print("\n\033[1;32;40m", i, " ",end="")

#Function to count letters in randomWord
def countLetters(word):
    global green
    global key
    global value
    green = {}  #store correct positions of letters
    yellow = {} #for occurences at wrong position
    k = 0
    for i in word:
        if i in randomWord:
            if word[k] == randomWord[k]:
                green[i] = k
        k += 1
    for i in randomWord:
        if i not in yellow:
            yellow[i] = 1
        else:
            yellow[i] += 1
    key = list(yellow)  #list to store letters with wrong position
    value = list(yellow.values()) #list to store count of occurence of letters with wrong position
    for i in value:
        i -= 1
    for i in key:
        if i in green:
            value[key.index(i)] -= 1

#Function to check yellow
def countForYellow(i):
    global key
    global value
    if i in key:
        x = key.index(i)
        if value[x] > 0:
            setYellow(i)
            value[x] -= 1
        else:
            setGray(i)    

#Function to check each letter if it is present in randomWord
def checkInput(word):
    global randomWord
    k = 0
    for i in word:
        if i in randomWord:
            #Checking position of letters and setting green if right position
            if word[k] == randomWord[k]:
                    setGreen(i)
            #Checking position of letters and setting yellow if wrong position
            else:
                countForYellow(i)
        else:
            setGray(i)
        k += 1
    clearColor()

#Function to check length, numbers and special characters in userInput
def checkNonChars():
    global userInput
    case1 = False; case2 = False
    if len(userInput) < 5:
        print("Not enough letters")
        return False
    if len(userInput) > 5:
        print("Only 5 letters allowed")
        return False
    for i in userInput:
        if i.isdigit():
            case1 = True
        elif not i.isalpha():
            case2 = True
    if case1 and case2:
        print("Numbers and Special characters not allowed")
        return False
    elif case1:
        print("Numbers not allowed")
        return False
    elif case2:
        print("Special characters not allwoed")
        return False        
    return True

#Function to print winning words according to how fast user guess the word
def checkOutput(chance):
    if chance == 1:
        boldGreen("Genius")
    elif chance == 2:
        boldGreen("Magnificient")
    elif chance == 3:
        boldGreen("Impressive")
    elif chance == 4:
        boldGreen("Splendid")
    elif chance == 5:
        boldGreen("Great")
    else:
        boldGreen("Phew")

#Function to check if entered string is in list and setting colors according to position
def userInputValidate(chance):
    global userInput
    global allInputs
    countLetters(userInput)
    givenFile = urllib.request.urlopen(wordListURL)
    for eachLine in givenFile:
        line = eachLine.decode("utf-8")
        if userInput in line:
            if(userInput == randomWord):
                for i in userInput:
                    setGreen(i)
                clearColor()
                checkOutput(chance)
                clearColor()
                print()
                sys.exit(1)
            else:
                checkInput(userInput)
                allInputs.append(userInput)
            return
    print("Not in word list")
    recall(chance)

#Function to recall if any error occur
def recall(chance):
    global userInput
    print("\n\033[1;30;47m Chance " , chance, " ", end="")
    clearColor()     
    print("\033[1;37;40mType help or ? for RULE BOOK  |  history or * to see all moves \033[0;37;48m\n")
    userInput = input("Enter 5 letter word: ").lower()
    if userInput == "help" or userInput == "?":
        rules()
        recall(chance)
    elif userInput == "history" or userInput == "*":
        history(chance)
        recall(chance)
    else:
        print()
        chk = checkNonChars()
        if chk:
            userInputValidate(chance)
        else:
            recall(chance)

#Function to print WORDLE if all chances missed
def hiddenWord():
    print("\033[1;37;40mSolution: \033[0;37;48m", end = "")
    temp = randomWord.title()
    for i in temp:
        setGreen(i)
    clearColor()

#Function to print valid user inputs from last moves
def history(chance):
    if chance == 1:
        print("\nNo word entered yet!")
        return
    print()
    for i in allInputs:
        countLetters(i)
        checkInput(i)

#Taking Input
#Main Function
def main():
    global userInput
    print("\n========= WORDLE ========= \n")
    rules()
    for i in range(6):
        recall(i+1)

    clearColor()
    hiddenWord()

if __name__ == "__main__":
    main()