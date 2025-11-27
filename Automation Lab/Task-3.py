import sys
import msvcrt

def gitbash_input(prompt):
    """Safe input method for Git Bash on Windows."""
    print(prompt, end=" ", flush=True)
    
    buffer = ""
    while True:
        char = msvcrt.getwch()
        if char == "\r":     # Enter key
            print()
            return buffer
        elif char == "\b":   # Backspace
            buffer = buffer[:-1]
            print("\b \b", end="", flush=True)
        else:
            buffer += char
            print(char, end="", flush=True)


def greet(name):
    print(f"Welcome {name}! Ready to automate?")


user = gitbash_input("Hello! Niharika:")
greet(user)

