from utils import clear, pause, slow_print
from art import CAT
from state import game_state

def level_one(game_state):
    clear()
    slow_print("Episode 1: The Anomaly")
    pause()

    slow_print("You wake up to a quiet morning. The sun is just beginning to rise, casting a warm glow over your surroundings. Everything seem normal, but slightly too still.")
    pause(1)

    slow_print("You notice a plant has grown overnight on the window sill. Not wildly, Just... intentionally.")
    pause(1)

    print("\nWhat do you do?")
    print("A. Inspect the plant closely.")
    print("B. Ignore it and go about your day.")
    print("C. look around to see if anything else is unusual.")
    choice = input("Choose A, B, or C: ").strip().upper()

    if choice == 'A':
        slow_print("Your fingers brush the leaves. They feel warm.")
        game_state['curiosity'] += 1
        game_state['connection'] += 1
    elif choice == 'B':
        slow_print("You decide to ignore the plant, but a nagging feeling lingers.")
        game_state['stability'] += 1
    elif choice == 'C':
        slow_print("Your instints are sharp. Something is observing you from the shadows.")
        game_state['curiosity'] += 1
        print(CAT)
        game_state['connection'] += 1
    pause(2)

