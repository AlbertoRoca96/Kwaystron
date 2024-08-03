# Project README
Hi my name is Alberto Roca the creator of this small prject. This Project took
place over the summer of 2024 from May 22nd - June 17th with the aid of Dr.
Robert Marmorstein.

## The Game
Well the game is very simple and the goal was to animate sprites and change screens overall which I did accomplish. Once you have ran the Kwaystron.prg file you simply use the arrow keys and try to get to the key. One pesky problem is the Wisp guarding it, if it touches you, it is respawn time. Good luck with this very simple game. 

## Overview

This project demonstrates how to assemble a `.asm` file into a `.prg` file for the Commodore 64 using the `64tass Turbo Assembler Macro V1.58.2974`. The provided Python script (`converter.py`) automates this process. You will also need the VICE emulator to run the generated `.prg` files.

## Prerequisites

- **64tass Turbo Assembler Macro V1.58.2974**
- **Python 3.x**
- **VICE Emulator**: To run the `.prg` files on your computer.
- **Vim (optional)**: For editing `.asm` and `.py` files

## Files

- `converter.py`: Python script to assemble `.asm` file into `.prg` file.
- `somethingnew.asm`: Example assembly source file.
- `listing.txt`: Output listing file generated during assembly.
- `Kwaystron.prg`: Example output `.prg` file.

## Usage

To assemble the `somethingnew.asm` file into a `.prg` file using the provided Python script, run the following command in your terminal:

sh
python3 converter.py somethingnew.asm Kwaystron.prg


