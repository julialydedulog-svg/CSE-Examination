# gps_tracker.py
def main() -> None:
    x, y = 0, 0
    print("GPS Tracker — start at (0, 0).")
    print('Enter N / S / E / W or full words North / South / East / West. Type "STOP" to finish.\n')

    while True:
        cmd = input("Enter direction (or STOP): ").strip().lower()

        # Exit condition
        if cmd == "stop":
            break

        # Move handling
        if cmd in ("n", "north"):
            y += 1
        elif cmd in ("s", "south"):
            y -= 1
        elif cmd in ("e", "east"):
            x += 1
        elif cmd in ("w", "west"):
            x -= 1
        else:
            print("Invalid input. Please enter N/S/E/W or North/South/East/West, or STOP to end.")
            continue  # ask again without changing position

        # Show current position after a valid move
        print(f"Current position: ({x}, {y})")

    # Session ended -> final summary
    print("\nSession ended.")
    print(f"Final position: ({x}, {y})")
    if x == 0 and y == 0:
        print("You returned to the origin (0, 0).")
    else:
        print("You did NOT return to the origin (0, 0).")

if __name__ == "__main__":
    main()
