# Hangman Game

A simple console-based Hangman game implemented in Python.

---

## Project Overview

This Hangman game allows a player to guess a hidden word one letter at a time. The player has limited lives, and a visual hangman figure updates with each wrong guess. The game ends when the player guesses the entire word or runs out of lives.

---

## Features

- Random word selection from a predefined list.
- Visual hangman stages displayed as ASCII art.
- Lives decrease with each incorrect guess.
- Display shows known letters and blanks for unknown letters.
- Simple start menu with screen clearing for better user experience.

---

## Files Description

- `hangman_game.py`: Contains the main game logic and user interaction.
- `hangman_stages.py`: Stores ASCII art stages for the hangman figure.
- `word_list.py`: Contains the list of words from which the game randomly chooses.
- `Main_Menu.py`: Displays a welcome menu and clears the screen before starting the game.

---

## How to Run

1. Make sure all files are in the same directory.
2. Run the main game file:

   ```bash
   python hangman_game.py
