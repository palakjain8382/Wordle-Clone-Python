# Wordle-Clone-Python
Wordle Clone in Python

This is a basic clone of the game WORDLE.
[Link](https://www.nytimes.com/games/wordle/index.html)

<h4>Wordle Game</h4>

The user gets six chances to guess a five-letter word.
According to the position of the hidden word, the letters are colored: yellow, green and grey.
Where yellow letters show that the letters are present in the hidden wordle. The letters that are in hidden word and input with the correct position are green. All other letters are grey i.e., those letters that are not in the hidden word.

<h4>Wordle Clone Game</h4>

The Wordle Clone Game is being designed in Python3.
This game is a command line application. Hence, it has some added functionalities to make the user experience better.
1. User can type '?' or 'help' to see the rules.
2. User can type '\*' or 'history' to see all inputs of the user. This clears the user's vision and makes the guessing process easy.
3. If the input holds more than 5 letters, numbers, or special characters, the user gets an error, and the chance will not be deducted.
4. Each input is checked if present in the repository [Link](https://raw.githubusercontent.com/charlesreid1/five-letter-words/master/sgb-words.txt). Else an error is thrown "Not in word list".
5. Inspired by the original game, the clone uses different winning words for each chance. For example, if the user guesses the word within the first move, he/she will be called "Genius".
6. If the user is unable to guess the word within six chances, the hidden word will be displayed.

Some screenshots of the Wordle Clone Game:
![image](https://user-images.githubusercontent.com/61820639/170128741-fa904a99-fcde-444f-bebe-996725905ad2.png)
![image](https://user-images.githubusercontent.com/61820639/170128856-58d14072-3e44-4edd-b142-96bcf0bf272d.png)
![image](https://user-images.githubusercontent.com/61820639/170130020-8755560e-1b2a-447f-a2ab-161509521a75.png)
