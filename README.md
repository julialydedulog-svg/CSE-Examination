# CSE-Examination

# gps_tracker.py
# -----------------------------------------------
# A simple Python program that simulates a GPS tracker.
# The player starts at (0,0) and can move North, South,
# East, or West based on user input.
# The program ends when the user types "STOP".
# -----------------------------------------------

def main() -> None:
    # Starting position at the origin
    x, y = 0, 0
    
    # Introductory instructions
    print("GPS Tracker — start at (0, 0).")
    print('Enter N / S / E / W or full words North / South / East / West. Type "STOP" to finish.\n')

    # Loop until the user enters STOP
    while True:
        # Get input, remove extra spaces, and convert to lowercase
        cmd = input("Enter direction (or STOP): ").strip().lower()

        # Check if the user wants to end the session
        if cmd == "stop":
            break

        # Process movement based on valid commands
        if cmd in ("n", "north"):      # Move North → increase y
            y += 1
        elif cmd in ("s", "south"):    # Move South → decrease y
            y -= 1
        elif cmd in ("e", "east"):     # Move East → increase x
            x += 1
        elif cmd in ("w", "west"):     # Move West → decrease x
            x -= 1
        else:
            # If the input is not recognized, show an error message
            print("Invalid input. Please enter N/S/E/W or North/South/East/West, or STOP to end.")
            continue  # Skip showing position, ask again for input

        # After a valid move, show the updated position
        print(f"Current position: ({x}, {y})")

    # Once the loop ends (STOP typed), show the final summary
    print("\nSession ended.")
    print(f"Final position: ({x}, {y})")
    
    # Check if the player returned to the origin (0, 0)
    if x == 0 and y == 0:
        print("You returned to the origin (0, 0).")
    else:
        print("You did NOT return to the origin (0, 0).")

# Entry point of the program
if __name__ == "__main__":
    main()


Key Explanations 

x, y = 0, 0 → the program starts at coordinate (0,0), which is the origin.

.strip().lower() → cleans the user input: removes extra spaces and converts everything to lowercase. This way, the program accepts inputs like " N ", "north", or "NORTH".

if cmd == "stop": break → this condition ends the loop when the user types STOP.

Movement rules:

North (n/north) → y + 1 (moves up)

South (s/south) → y - 1 (moves down)

East (e/east) → x + 1 (moves right)

West (w/west) → x - 1 (moves left)

Invalid input → if the user types something else, the program shows an error message and ignores the move.

After STOP → the program shows the final position and tells whether the player returned to the origin (0,0) or not.
