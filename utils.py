import os
import time

def clear():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(seconds=1.5):
    """Pause execution for a given number of seconds."""
    time.sleep(seconds)

def slow_print(text, delay=0.03):
    """Print text to the console one character at a time with a delay."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # For a new line after the text is printed