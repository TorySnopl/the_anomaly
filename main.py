from utils import clear, pause, slow_print
from state import game_state
from levels import level_one
from endings import show_ending

def main():
    clear()
    slow_print("A fringe event has been detected.")
    pause(1)

    # Start Level One
    level_one(game_state)

    # Show Ending based on final game state
    show_ending(game_state)

if __name__ == "__main__":
    main()