def gps_tracker():
    # Starting position
    x, y = 0, 0
    print("Starting at position (0, 0). Enter 'STOP' to end session.")

    # Movement mapping
    moves = {
        "n": (0, 1), "north": (0, 1),
        "s": (0, -1), "south": (0, -1),
        "e": (1, 0), "east": (1, 0),
        "w": (-1, 0), "west": (-1, 0),
    }

    while True:
        # User input
        command = input("Enter direction (N/S/E/W or STOP): ").strip().lower()

        if command == "stop":
            break

        if command in moves:
            dx, dy = moves[command]
            x += dx
            y += dy
            print(f"Current position: ({x}, {y})")
        else:
            print("❌ Invalid input! Use N, S, E, W or STOP.")

    # End of session
    print("\nSession ended.")
    print(f"Final position: ({x}, {y})")
    print("You returned to origin (0,0)." if (x, y) == (0, 0) else "You did NOT return to origin.")


# Run the program
gps_tracker()
