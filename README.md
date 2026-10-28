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
your current room, and `status` to check your progress.

| Command | What it does |
| --- | --- |
| `go [direction]` | Move north, south, east, or west |
| `get [item]` | Pick up the visible item in the room |
| `status` | Show your room, inventory, and artifact count |
| `help` | Display the available commands |
| `exit` | Quit the game |

Example:

```text
go north
get ancient spellbook
status
```

### 🏆 The goal

Collect all seven artifacts before entering the Throne Room. The Silver Key is
in the Dungeon and is required to unlock its door. The key opens the way, but
you still need the complete artifact collection to defeat Malachar.

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
uppercase commands, inventory display, item collection, the locked Throne Room,
and both game endings.

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
