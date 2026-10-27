# 🏰 The Arcane Tower Adventure

A fantasy text-based adventure game built with Python. Players navigate a mysterious tower, solve environmental puzzles, and gather magical artifacts to face a powerful sorcerer.

## 📖 Game Overview
You are a wizard apprentice who has entered the prestigious Arcane Tower, only to discover that the evil sorcerer Malachar has seized control. Your mission is to navigate the tower's various chambers, find the hidden artifacts, and confront Malachar in the Throne Room.

## 🎯 Objectives & Gameplay
*   **Primary Goal:** Collect all **seven** legendary magical artifacts hidden throughout the tower.
*   **Navigation:** Move freely between rooms (North, South, East, West).
*   **Interaction:** Locate and "Get" items from specific rooms.
*   **Status:** Keep track of your current location and your inventory at any time.

## 🏆 Win/Loss Conditions
*   **Victory:** You win by reaching the **Throne Room** while carrying all seven artifacts in your inventory. This triggers the final victory sequence.
*   **Defeat:** If you enter the **Throne Room** without all seven artifacts, Malachar will defeat you instantly. 

## 🛠 Features
- **Dynamic Room Mapping:** Uses nested dictionaries to manage world exploration.
- **Inventory System:** Tracks items collected and updates the "Visible Item" status in real-time.
- **Input Validation:** Handles invalid directions and incorrect item names gracefully.
- **Modular Code:** Built using independent functions for movement, status updates, and item collection to ensure clean, readable code.

## 🚀 How to Run
1. Ensure you have Python installed on your computer.
2. Download the `TextBasedGame.py` file.
3. Open your terminal or command prompt.
4. Navigate to the folder and run:
   ```bash
   python TextBasedGame.py

🎓 Learning Milestones
 Dictionary manipulation and data structures.
 String parsing and user input handling.
 Implementing game loops and state management.
 Clean code practices and functional programming.