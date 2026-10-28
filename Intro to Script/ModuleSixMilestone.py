# Christopher Matchett

# The dictionary linking rooms
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

# Start player in Great Hall
current_room = 'Great Hall'

# Gameplay loop continues until player enters "exit" room
while current_room != 'exit':
    # Displays the player's current location
    print(f"You are in the {current_room}")

    # Prompt the player for a command
    command = input("Enter command: ").strip()

    # Handle the player's command
    if command == 'exit':
        current_room = 'exit'
    elif len(command.split()) >= 2 and command.split()[0] == 'go':
        parts = command.split()
        direction = parts[1].capitalize()
        if current_room in rooms and direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("Invalid move")
    else:
        print("Invalid command")

# Final message once the loop end
print("\nYou have exited the game. Thanks for playing!")
