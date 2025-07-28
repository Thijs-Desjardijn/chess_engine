Chess Engine
This is a Python-based chess engine that uses an opening book and a Minimax algorithm with alpha-beta pruning to evaluate and select moves. It is designed to be an intermediate-level chess engine.

Features
Python implementation

Minimax algorithm for move decision

Alpha-beta pruning for performance

Opening book support

Modular and extendable codebase

Installation
To use this engine, you'll need uv, a fast Python package manager. If you don’t already have it installed, follow the instructions on the [uv GitHub page](https://github.com/astral-sh/uv).

Once uv is installed, add the project with:

uv add https://github.com/Thijs-Desjardijn/chess_engine

Usage
To run the engine, use:

uv run main.py

This is solely a chess engine and does not include a graphical interface like Pygame. You can play a game against the engine using UCI-style move notation, for example:

e2e4 — move a pawn from e2 to e4
e7e8q — promote a pawn to a queen on e8

Requirements
Python 3.8+

uv (for installation and dependency management)