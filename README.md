
# 🃏 Blackjack Game - Python CLI

## 📋 Description

This is a basic implementation of the Blackjack card game (also known as 21) using Python. The game lets a user and a computer take random turns. Each tries to get as close to 21 as possible without going over ("busting"). The game includes initial blackjack detection, turn-based card drawing ("hit" or "skip"), and win/lose logic.

## 🎮 Features

- Randomly decides whether the user or computer goes first.
- Simulates a deck with values: 1–10, face cards as 10, Ace as 11.
- Detects instant Blackjack (21 in 2 cards).
- User can input to "hit" (draw another card) or "skip" (stand).
- Computer randomly decides to hit or skip.
- Automatically checks for busts and declares the winner.
- Uses Python's built-in `random` module only.

## ▶️ How to Run

Make sure Python is installed on your system. Then run:

```
python game_blackjack.py
```

## 🗂️ File Structure

- `game_blackjack.py` — contains all the game logic and rules.

## ✅ Example Output

```
Turn: user
Your cards: [10, 6] (Total: 16)
Computer's first card: 7
Tell y to hit and n to skip: y
New user cards: [10, 6, 4] (Total: 20)
Computer chose to skip.
Final user cards: [10, 6, 4] (Total: 20)
Final computer cards: [7, 8] (Total: 15)
User Wins
Game Over
```

## 📌 Notes

- Ace is always treated as 11 in this version.
- Game is single-round only.
- For simplicity, cards are not removed from the deck after drawing.

## 🔧 Requirements

- Python 3.x
- No external libraries required
