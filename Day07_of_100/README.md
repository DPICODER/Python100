# Hangman Game

## Introduction
Welcome to the Hangman Game! In this classic word-guessing game, you have to guess the letters of a randomly selected word. Each incorrect guess results in losing a life, represented by the hangman figure. Your goal is to guess the word before running out of lives.

### Getting Started
To play the Hangman Game, run the provided Python script. Follow the on-screen instructions to input your guesses and try to reveal the hidden word.

```python
python hangman_game.py
```

### Rules
1. You start with 6 lives.
2. Enter a letter as your guess to uncover the word.
3. If your guess is correct, the corresponding letters will be revealed.
4. If your guess is incorrect, you lose a life, and part of the hangman figure is displayed.
5. The game ends when you either correctly guess the entire word or run out of lives.

### Functions and Components
- **Random Word:** A random word is generated from a predefined list of words.
- **Word Length:** The length of the word is determined to create placeholders for display.
- **Display:** A list of placeholders representing the word, initially filled with underscores.
- **Lives:** You start with 6 lives, and each incorrect guess deducts a life.
- **End State:** The game continues until you either correctly guess the word or run out of lives.

### ASCII Art Hangman
As you make incorrect guesses, the hangman figure is displayed in ASCII art. The goal is to avoid losing all lives and revealing the entire hangman figure.

### Winning and Losing
- **Winning:** If you successfully guess all the letters and uncover the word, you win!
- **Losing:** If you run out of lives, the game ends, and you lose.

### Enjoy Playing Hangman!
Thank you for playing the Hangman Game! Whether you're a word-guessing pro or just getting started, we hope you enjoy the challenge. If you have any feedback or suggestions, feel free to share them. Happy guessing!