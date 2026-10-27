# TextBasedGame.py
# Author: Christopher Matchett

"""
The Arcane Tower Adventure
A fantasy text-based adventure game where the player must collect all seven
legendary magical artifacts before confronting the evil sorcerer Malachar
in the Throne Room.
"""


# Display available commands to the player
def show_instructions():
    print("\n========= THE ARCANE TOWER =========")
    print("Commands:")
    print("  go [direction]  - Move North, South, East, or West")
    print("  get [item]      - Pick up an item in the current room")
    print("  status          - Show current room, inventory, and visible item")
    print("  help            - Show this help message")
    print("  exit            - Quit the game")
    print("====================================\n")


# Display the player's current room, inventory, and visible item
def show_status(current_room, inventory, room_items):
    print("\n---------------------------")
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")
    if room_items[current_room] is not None:
        print(f"Visible item: {room_items[current_room]}")
    print("---------------------------\n")


# Move the player in the given direction if possible
def move_player(current_room, direction, rooms):
    direction = direction.capitalize()

    if direction not in ('North', 'South', 'East', 'West'):
        print("\n*** Invalid direction ***")
        print("Please enter North, South, East, or West.")
        return current_room, False

    new_room = rooms[current_room].get(direction)

    if new_room is None:
        print("\n*** You cannot go that way ***")
        return current_room, False

    print(f"\nYou moved {direction} to: {new_room}")
    return new_room, True


# Pick up an item from the current room and update inventory
def get_item(current_room, item_name, inventory, room_items):
    expected_item = room_items[current_room]

    if expected_item is None:
        print("\n*** There is no item to pick up in this room. ***")
        return inventory

    if item_name.lower() != expected_item.lower():
        print("\n*** That item is not in this room. ***")
        print(f"The item here is the {expected_item}.")
        return inventory

    if expected_item in inventory:
        print(f"\nYou already have the {expected_item}.")
        return inventory

    inventory.append(expected_item)
    room_items[current_room] = None
    print(f"\nYou picked up the {expected_item}!")
    return inventory


# Main gameplay loop
def main():

    # Dictionary linking the nine rooms
    rooms = {
        'Entrance': {
            'North': 'Library',
            'South': 'Dungeon',
            'East': 'Armory',
            'West': 'Garden'
        },
        'Library': {
            'South': 'Entrance',
            'East': 'Alchemy Lab',
            'West': 'Observatory'
        },
        'Alchemy Lab': {
            'West': 'Library'
        },
        'Observatory': {
            'South': 'Garden',
            'East': 'Library'
        },
        'Armory': {
            'North': 'Secret Chamber',
            'West': 'Entrance'
        },
        'Garden': {
            'North': 'Observatory',
            'East': 'Entrance'
        },
        'Dungeon': {
            'North': 'Entrance',
            'East': 'Throne Room'
        },
        'Secret Chamber': {
            'South': 'Armory'
        },
        'Throne Room': {
            'West': 'Dungeon'
        }
    }

    # Dictionary mapping each room to item
    room_items = {
        'Entrance': None,
        'Library': 'Ancient Spellbook',
        'Alchemy Lab': 'Magic Potion',
        'Observatory': 'Star Chart',
        'Garden': 'Enchanted Flower',
        'Armory': 'Crystal Sword',
        'Dungeon': 'Silver Key',
        'Secret Chamber': 'Mystic Amulet',
        'Throne Room': None
    }

    # Total number of collectible items
    total_items = 7

    # Player state
    current_room = 'Entrance'
    inventory = []

    print("=" * 50)
    print("  THE ARCANE TOWER ADVENTURE")
    print("=" * 50)
    print("You are a young wizard apprentice entering the")
    print("prestigious Arcane Tower, only to discover the")
    print("evil sorcerer Malachar has seized control!")
    print("Collect all 7 legendary artifacts before facing")
    print("Malachar in the Throne Room.\n")

    show_instructions()
    show_status(current_room, inventory, room_items)

    # Main gameplay loop
    while current_room != 'exit':
        command = input("Enter command: ").strip()

        # Exit the game
        if command == 'exit':
            current_room = 'exit'

        # Show instructions
        elif command == 'help':
            show_instructions()

        # Show player status
        elif command == 'status':
            show_status(current_room, inventory, room_items)

        # Move between rooms
        elif len(command.split()) >= 2 and command.split()[0] == 'go':
            direction = command.split()[1]
            current_room, moved = move_player(current_room, direction, rooms)

            if moved:
                # Check for villain encounter after moving
                if current_room == 'Throne Room':
                    if len(inventory) == total_items:
                        print("\n*** YOU CONFRONT MALACHAR ***")
                        print("Wielding all seven legendary artifacts, you")
                        print("unleash a blinding burst of arcane power!")
                        print("Malachar is defeated and the tower is freed!")
                        print("\n*** CONGRATULATIONS! YOU WIN! ***")
                        current_room = 'exit'
                    else:
                        missing = total_items - len(inventory)
                        print(f"\n*** MALACHAR THE DARK SORCERER STANDS BEFORE YOU ***")
                        print(f"You are missing {missing} artifact(s)!")
                        print("Without the full power of the artifacts, you")
                        print("are no match for Malachar's forbidden magic.")
                        print("\n*** GAME OVER. You have been defeated. ***")
                        current_room = 'exit'
                else:
                    show_status(current_room, inventory, room_items)

        # Pick up an item
        elif len(command.split()) >= 2 and command.split()[0].lower() == 'get':
            item_name = command[4:].strip()
            inventory = get_item(current_room, item_name, inventory, room_items)
            show_status(current_room, inventory, room_items)

        # Invalid command
        else:
            print("\n*** Invalid command ***")
            print("Type 'help' to see the list of valid commands.")

    print("\nThanks for playing! Farewell, apprentice.")


# Start the game
if __name__ == '__main__':
    main()