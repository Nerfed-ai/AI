# Mini Text Adventure

This repository contains a minimal Python text adventure. The game runs in the
terminal and supports a handful of simple commands so you can explore a tiny
world and pick up a single item.

## Requirements

- Python 3.11+
- [pytest](https://pytest.org/) for running the automated tests

## Running the game

```bash
python game.py
```

When the game starts you will automatically receive a description of your
surroundings. Type commands such as `look`, `go north`, or `take lantern` to
interact with the world. Type `quit` to exit.

## Running the tests

Install the development requirements (pytest) and then run:

```bash
pytest
```
