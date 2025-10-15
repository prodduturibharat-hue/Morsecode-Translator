import tkinter as tk
from tkinter import messagebox, simpledialog

# Dictionary representing the Morse code chart
MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ",": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}

# Function to encrypt the string according to the Morse code chart
def encrypt(message):
    cipher = ""
    for letter in message.upper():
        if letter != " ":
            cipher += MORSE_CODE_DICT.get(letter, "") + " "
        else:
            cipher += " "
    return cipher

# Main program
def main():
    # Create a simple window
    root = tk.Tk()
    root.withdraw()  # Hide the main window (we just want dialog boxes)

    # Get user input
    message = simpledialog.askstring("Morse Code Converter", "Enter an English word or sentence:")

    if message:
        result = encrypt(message)
        messagebox.showinfo("Morse Code Result", f"Input: {message}\n\nMorse Code:\n{result}")
    else:
        messagebox.showwarning("No Input", "You didn't enter any text!")

# Executes the main function
if __name__ == "__main__":
    main()

