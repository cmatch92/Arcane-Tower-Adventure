# 🏰 The Arcane Tower Adventure

<p align="center">
  <img src="assets/arcane-tower.svg" alt="An enchanted tower beneath a starry night sky" width="720">
</p>

<p align="center">
  <strong>A command-line fantasy adventure built with Python</strong><br>
  Explore the tower. Recover its artifacts. Face Malachar.
</p>

---

## 📖 The story

You are a wizard apprentice entering the prestigious Arcane Tower. The evil
sorcerer Malachar has seized control, and seven legendary artifacts are hidden
throughout its chambers. Explore the tower, gather the complete collection, and
challenge Malachar in the Throne Room.

## ✨ Features

- 🗺️ **Room-based exploration** across nine connected locations.
- 🧙 **Seven collectible artifacts** with live inventory and progress updates.
- ⌨️ **Case-insensitive commands** for a forgiving, easy-to-use interface.
- 🧩 **Six riddle-locked doors:** solve the keyboard, towel, five, charcoal,
  candy, and gas riddles to explore the tower.
- 🔐 **A key-and-lock puzzle:** find the Silver Key in the Dungeon to unlock the
  route to the Throne Room.
- 🏆 **Two possible endings:** win with all seven artifacts, or face defeat if
  you enter the Throne Room unprepared.
- 🧪 **Automated tests** for commands, item collection, the locked route, and
  both endings.

## 🚀 Get started

### Requirements

- Python 3.11 or newer
- No third-party packages

### Run the game

Clone or download the repository, open a terminal in the project directory, and
run:

```bash
python TextBasedGame.py
```

## 🎮 How to play

Commands are case-insensitive. Use `go` to move, `get` to collect the item in
your current room, `answer` to solve a locked-door riddle, and `status` to
check your progress.

| Command | What it does |
| --- | --- |
| `go [direction]` | Move north, south, east, or west |
| `get [item]` | Pick up the visible item in the room |
| `answer [riddle]` | Answer the riddle at a locked door |
| `status` | Show your room, inventory, and artifact count |
| `help` | Display the available commands |
| `exit` | Quit the game |

Example:

```text
go north
get ancient spellbook
status
```

Try a locked door to hear its riddle, then type your answer directly. For
example, in the Armory, go north and enter `keyboard` to unlock the Secret
Chamber door. You can also use the `answer [riddle]` command.

| Door | Riddle | Answer |
| --- | --- | --- |
| Entrance–Dungeon | Remove two letters from “five” to make “four.” What are the letters? | `IV` (case-insensitive) |
| Entrance–Armory | Black when bought, red when used, white when discarded | `charcoal` |
| Library–Alchemy Lab | What gets wetter the more it dries? | `towel` or `a towel` |
| Armory–Secret Chamber | What has keys but no locks, and an Enter but no exit? | `keyboard` or `a keyboard` |
| Library–Observatory | Spell Candy with 2 letters. | `C and Y` (spell out “and”; case-insensitive) |
| Garden–Observatory | What is a 3 letter word that starts with gas? | `car` |

### 🏆 The goal

Collect all seven artifacts before entering the Throne Room. Solve the riddles
to explore the tower and reach the Secret Chamber and its Mystic Amulet. The
Silver Key is in the Dungeon and is required to unlock the Throne Room door. The
key opens the way, but you still need the complete artifact collection to
defeat Malachar.

### 🧿 Artifact locations

| Room | Artifact |
| --- | --- |
| Library | Ancient Spellbook |
| Alchemy Lab | Magic Potion |
| Observatory | Star Chart |
| Garden | Enchanted Flower |
| Armory | Crystal Sword |
| Dungeon | Silver Key |
| Secret Chamber | Mystic Amulet |

The Throne Room is the final destination; it contains no artifact.

## 🧪 Run the tests

The test suite uses Python's built-in `unittest` framework and requires no
additional dependencies:

```bash
python -m unittest -v
```

Tests simulate player input, so they run without manual interaction. They cover
uppercase commands, inventory display, item collection, all locked doors,
riddle answers, and both game endings.

## 📁 Project structure

```text
TextBasedGame.py          Game implementation
test_game.py              Automated unit and end-to-end tests
assets/arcane-tower.svg   Original README banner illustration
README.md                 Project documentation
```

## 🛠️ Built with

- **Python** — game logic and command-line interface
- **unittest** — automated testing
- **SVG** — original, locally stored README artwork
