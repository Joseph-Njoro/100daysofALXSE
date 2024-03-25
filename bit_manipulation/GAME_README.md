# Bit Manipulation Game

This is a simple console-based game where two players take turns entering their chosen bit patterns to achieve a target bit pattern through logical AND, OR, or XOR operations.

## How to Play

1. **Objective**: The objective of the game is to be the first player to achieve the target bit pattern through logical operations.

2. **Starting the Game**: Run the executable `game` to start the game.

3. **Game Setup**: The game will display the target bit pattern (a number between 0 and 15). Each player will take turns entering their chosen bit patterns.

4. **Player Turns**: 
    - Player 1 will be prompted to enter their bit pattern.
    - Player 2 will then be prompted to enter their bit pattern.

5. **Winning Condition**: If either player achieves the target bit pattern through AND, OR, or XOR operations, the game will declare them as the winner and end.

6. **Repeating the Game**: If no player achieves the target bit pattern, the game will continue with additional rounds until a winner is determined.

## Input Guidelines

- **Bit Patterns**: Players should enter their chosen bit patterns as integers between 0 and 15.
- **Valid Input**: The game validates input to ensure it falls within the acceptable range.
- **Invalid Input**: If a player enters invalid input (e.g., a negative number or a number greater than 15), they will be prompted to re-enter their bit pattern.

## Example

Welcome to the Bit Manipulation Game!
The target bit pattern is: 15

Player 1's turn:
Enter your bit pattern (0-15): 7
Player 2's turn:
Enter your bit pattern (0-15): 8

Sorry, neither player has achieved the target bit pattern yet. Keep trying!

Player 1's turn:
Enter your bit pattern (0-15): 14
Player 2's turn:
Enter your bit pattern (0-15): 1

Congratulations! One of the players has achieved the target bit pattern (15).


## Credits

Created by Joseph Njoroge