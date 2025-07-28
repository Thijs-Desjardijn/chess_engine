# Chess Engine

This is a Python-based chess engine that uses **square tables** and a **Minimax algorithm** with **alpha-beta pruning** to evaluate and select moves. It is designed to be an **intermediate-level chess engine**.

## Features

- Minimax algorithm for move decision  
- Alpha-beta pruning for performance  
- Square tables for positional play

## Installation

To use this engine, you'll need [**uv**](https://github.com/astral-sh/uv), a fast Python package manager.  
If you don’t already have it installed, follow the instructions on the [uv GitHub page](https://github.com/astral-sh/uv).

You will also have to initialize a git environment using:
```bash
git init
```
After that use:
```bash
git pull https://github.com/Thijs-Desjardijn/chess_engine
```
This will add the project to your foler.

## usage

To run the program use:

```bash
uv run main.py
```
This will start a game against the engine with you playing as white. The program uses **UCI format** (e2e4 for moving and e7e8q for promotions e.g.).
