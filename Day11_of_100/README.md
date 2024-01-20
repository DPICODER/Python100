# Black_Jack Beta v0.1

## Capstone Project: A Mix of All Methods Used from Day 1 to 10

### Introduction
Welcome to Black_Jack Beta v0.1! This is a simple console-based implementation of the classic Blackjack card game. The game is a culmination of various methods learned and applied from day 1 to 10 of the Capstone project.

### Getting Started
To play the game, simply run the provided Python script. You'll be prompted to press Enter to start the game. Follow the on-screen instructions to play the game, and enjoy the thrill of Blackjack!

```python
python Capstone_Project.py
```

### Game Rules
1. The game follows standard Blackjack rules.
2. You and the system (computer) are dealt two cards initially.
3. Your goal is to have a hand value as close to 21 as possible without exceeding it.
4. Face cards (Jack, Queen, King) have a value of 10, and Aces can be either 1 or 11.
5. If your initial two cards sum to 21, you have a Blackjack.
6. You can choose to draw additional cards ("hit") or pass ("stand").
7. The system will then draw cards until its total is 17 or higher.
8. The winner is determined based on the total value of the cards, with special considerations for Blackjacks.

### Game Functions
- `welcome()`: Displays a welcome message and invokes the gamestart function.
- `card_sum(cards)`: Evaluates the total value of a set of cards, considering the special case of having an Ace.
- `gamestart()`: Main game function that manages the flow of the game.
- `card_drawer()`: Draws a random card from the deck.
- `compare(user_score, sys_score)`: Compares the scores of the player and the system to determine the winner.

### Playing Another Round
After completing a round, you have the option to play another game of Blackjack. Simply type 'y' if you want to continue or 'n' if you wish to exit.

### Enjoy Your Game!
Thank you for playing Black_Jack Beta v0.1! Have fun, and may the cards be in your favor. If you encounter any issues or have suggestions for improvement, feel free to let us know. Happy gaming!