# Mini Pikachu Desktop Buddy

A small desktop application written in Python using PyQt5 that displays an animated Pikachu moving around the screen.  
The program creates a transparent, always-on-top window and controls the sprite’s movement using simple behavior logic.

---

## Functionality

- Displays an animated GIF in a frameless, transparent window
- Keeps the window always on top of other applications
- Moves the sprite around the screen at fixed time intervals
- Uses two movement modes:
  - Random wandering
  - Smooth mouse-following behavior
- Ensures the sprite stays within screen bounds
- Allows the program to be closed via right-click on the sprite

---

## How It Works

- A `QLabel` is used as the window container
- A `QMovie` is used to render the animated GIF
- A `QTimer` updates the sprite position periodically
- Mouse position is read using `QCursor`
- Movement logic interpolates toward the mouse when in follow mode
- Position clamping prevents the sprite from leaving the visible screen

---

## Requirements

- Python 3.8 or newer
- PyQt5

Install dependencies:
```bash
pip install PyQt5

To run execute this command on the terminal
python pikachu.py

This project does not modify system files, does not run on startup, and does not collect any data.
It is intended purely as a small graphical experiment and learning project.


## Future Plans

I plan on optimizing movement by creating different animations so it flows more smoothly as opposed to a single gif.
Eventually more pokemon will be added and so will interaction between them.
