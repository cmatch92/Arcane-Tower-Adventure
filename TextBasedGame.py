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
def show_status(current_room, inventory, room_items, room_descriptions, required_artifacts):
    print("\n---------------------------")
    print(f"You are in the {current_room}")
    print(f"Description: {room_descriptions[current_room]}")

    if not inventory:
        print("Inventory: Your pack is empty.")
    else:
        # List artifacts clearly
        items_list = ", ".join(inventory)
        print(f"Inventory: {items_list}")

    print(f"Artifacts collected: {len(inventory)} / {len(required_artifacts)}")

    if room_items[current_room] is not None:
        print(f"Visible item: {room_items[current_room]}")
    print("---------------------------\n")


# Move the player in the given direction if possible
def move_player(current_room, direction, rooms, inventory):
    direction = direction.strip().capitalize()

    if direction not in ('North', 'South', 'East', 'West'):
        print("\n*** Invalid direction ***")
        print("Please enter North, South, East, or West.")
        return current_room, False

    new_room = rooms[current_room].get(direction)

    if new_room is None:
        print("\n*** You cannot go that way ***")
        return current_room, False

    # Silver Key Puzzle: Unlock Throne Room from Dungeon
    if current_room == 'Dungeon' and new_room == 'Throne Room':
        if 'Silver Key' not in inventory:
            print("\n*** The heavy iron door to the Throne Room is locked! ***")
            print("You need a Silver Key to unlock it.")
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

    # Descriptions shown whenever the player views a room
    room_descriptions = {
        'Entrance': 'A tall vaulted hall, lit by a faint blue glow, welcomes you into the tower.',
        'Library': 'Dusty shelves rise to the ceiling, packed with books that whisper softly.',
        'Alchemy Lab': 'Bubbling glass vessels cast strange colors across the cluttered worktables.',
        'Observatory': 'A brass telescope points through the open dome toward a sky full of stars.',
        'Garden': 'Silver leaves shimmer among winding paths and luminous flowers.',
        'Armory': 'Old suits of armor stand watch beside racks of finely crafted weapons.',
        'Dungeon': 'Cold stone walls close in around rusted bars and a damp, shadowy floor.',
        'Secret Chamber': 'A hidden room glimmers with ancient runes etched into its walls.',
        'Throne Room': 'A black stone throne looms beneath banners darkened by sorcery.'
    }

    # Explicitly define required artifacts
    required_artifacts = [
        'Ancient Spellbook',
        'Magic Potion',
        'Star Chart',
        'Enchanted Flower',
        'Crystal Sword',
        'Silver Key',
        'Mystic Amulet'
    ]

    # Player state
    current_room = 'Entrance'
    inventory = []

    print("=" * 50)
    print("  THE ARCANE TOWER ADVENTURE")
    print("=" * 50)
    print("You are a young wizard apprentice entering the")
    print("prestigious Arcane Tower, only to discover the")
    print("evil sorcerer Malachar has seized control!")
    print(f"Collect all {len(required_artifacts)} legendary artifacts before facing")
    print("Malachar in the Throne Room.\n")

    show_instructions()
    show_status(current_room, inventory, room_items, room_descriptions, required_artifacts)

    # Main gameplay loop
    running = True
    while running:
        try:
            command = input("Enter command: ").strip()
        except EOFError:
            break

        # Case-insensitive command handling
        cmd_lower = command.lower()

        # Exit the game
        if cmd_lower == 'exit':
            running = False

        # Show instructions
        elif cmd_lower == 'help':
            show_instructions()

        # Show player status
        elif cmd_lower == 'status':
            show_status(current_room, inventory, room_items, room_descriptions, required_artifacts)

        # Move between rooms
        elif cmd_lower.startswith('go '):
            parts = command.split(maxsplit=1)
            if len(parts) < 2:
                print("\n*** Please specify a direction (e.g., 'go North') ***")
                continue
            direction = parts[1]
            current_room, moved = move_player(current_room, direction, rooms, inventory)

            if moved:
                show_status(current_room, inventory, room_items, room_descriptions, required_artifacts)

                # Check for villain encounter after moving
                if current_room == 'Throne Room':
                    # Victory condition: check if player has all required artifacts
                    has_all = all(item in inventory for item in required_artifacts)
                    if has_all:
                        print("\n*** YOU CONFRONT MALACHAR ***")
                        print("Wielding all seven legendary artifacts, you")
                        print("unleash a blinding burst of arcane power!")
                        print("Malachar is defeated and the tower is freed!")
                        print("\n*** CONGRATULATIONS! YOU WIN! ***")
                        running = False
                    else:
                        # Calculate missing artifacts
                        missing_items = [item for item in required_artifacts if item not in inventory]
                        print(f"\n*** MALACHAR THE DARK SORCERER STANDS BEFORE YOU ***")
                        print(f"You are missing {len(missing_items)} artifact(s)!")
                        print("Without the full power of the artifacts, you")
                        print("are no match for Malachar's forbidden magic.")
                        print("\n*** GAME OVER. You have been defeated. ***")
                        running = False

        # Pick up an item
        elif cmd_lower.startswith('get '):
            parts = command.split(maxsplit=1)
            if len(parts) < 2:
                print("\n*** Please specify an item to get (e.g., 'get Silver Key') ***")
                continue
            item_name = parts[1]
            inventory = get_item(current_room, item_name, inventory, room_items)
            show_status(current_room, inventory, room_items, room_descriptions, required_artifacts)

        # Invalid command
        else:
            print("\n*** Invalid command ***")
            print("Type 'help' to see the list of valid commands.")

    print("\nThanks for playing! Farewell, apprentice.")


# Start the game
if __name__ == '__main__':
    main()
