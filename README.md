# Random Password Generator (Tkinter)

A **GUI-based password generator** built with Python and Tkinter. Allows users to create secure random passwords with customizable options.

## Features

* Specify password length (8–32 characters)
* Include/exclude:

  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Symbols
* Generates a random password meeting selected criteria
* Copy generated password directly to clipboard
* Simple, user-friendly interface

## How to Run

1. Install dependencies:

```bash
pip install pyperclip tkmacosx
```

2. Run the script:

```bash
python3 password_generator.py
```

3. Enter your desired length, select character options, and click **Generate**.
4. Click **Copy to Clipboard** to use your password elsewhere.

## Notes

* Password length must be between 8 and 32 characters
* At least one character type must be selected
