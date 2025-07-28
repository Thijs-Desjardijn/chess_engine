# Chess Engine
# Chess Engine

This is a Python-based chess engine that uses an opening book and a Minimax algorithm with **alpha-beta pruning** to evaluate and select moves. It is designed to be an **intermediate-level chess engine**.
This is a Python-based chess engine that uses an opening book and a Minimax algorithm with **alpha-beta pruning** to evaluate and select moves. It is designed to be an **intermediate-level chess engine**.

## Features
## Features

- Minimax algorithm for move decision  
- Alpha-beta pruning for performance  
- Opening book support
- Minimax algorithm for move decision  
- Alpha-beta pruning for performance  
- Opening book support

## Installation
## Installation

To use this engine, you'll need [**uv**](https://github.com/astral-sh/uv), a fast Python package manager.  
If you don’t already have it installed, follow the instructions on the [uv GitHub page](https://github.com/astral-sh/uv).
To use this engine, you'll need [**uv**](https://github.com/astral-sh/uv), a fast Python package manager.  
If you don’t already have it installed, follow the instructions on the [uv GitHub page](https://github.com/astral-sh/uv).

Once `uv` is installed, add the project with:
Once `uv` is installed, add the project with:

```bash
```bash
uv add https://github.com/Thijs-Desjardijn/chess_engine
```
## usage
```
## usage

To run the program use:
To run the program use:

```bash
```bash
uv run main.py
```
This will start a game against the engine with you playing as white. The program uses **UCI format** (e2e4 for moving and e7e8q for promotions e.g.).