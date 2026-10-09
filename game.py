"""Minimal text adventure game.

This module contains a small text adventure with a handful of
commands to demonstrate the game loop and command handling.
"""

from __future__ import annotations


def normalize(command: str) -> str:
    """Normalize user input by trimming whitespace and lowering case."""
    return command.strip().lower()


class Game:
    """A tiny adventure featuring two rooms and a single item."""

    def __init__(self) -> None:
        self.rooms = {
            "clearing": {
                "description": (
                    "You stand in a forest clearing. A mossy path leads north to a cottage."
                ),
                "exits": {"north": "cottage"},
                "items": ["lantern"],
            },
            "cottage": {
                "description": (
                    "You step inside a quiet cottage. A warm fireplace glows here. The door leads south."
                ),
                "exits": {"south": "clearing"},
            },
        }
        self.location = "clearing"
        self.inventory: list[str] = []

    def describe_location(self) -> str:
        """Return a description of the current room."""
        room = self.rooms[self.location]
        description = room["description"]
        items = room.get("items", [])
        if items:
            item_list = ", ".join(items)
            description += f"\nYou see {item_list}."
        exits = ", ".join(sorted(room["exits"].keys()))
        description += f"\nExits: {exits}."
        return description

    def process_command(self, command: str) -> str:
        """Handle a player command and return the resulting message."""
        command = normalize(command)
        if not command:
            return "You must say something."

        if command in {"look", "l"}:
            return self.describe_location()

        words = command.split()
        verb = words[0]

        if verb == "go" and len(words) > 1:
            return self._handle_go(words[1])
        if verb == "take" and len(words) > 1:
            return self._handle_take(words[1])
        if verb in {"inventory", "i"}:
            return self._handle_inventory()
        if verb in {"quit", "exit"}:
            return "Thanks for playing!"

        return "You can't do that."

    def _handle_go(self, direction: str) -> str:
        room = self.rooms[self.location]
        target = room["exits"].get(direction)
        if not target:
            return "You can't go that way."
        self.location = target
        return self.describe_location()

    def _handle_take(self, item: str) -> str:
        room = self.rooms[self.location]
        items = room.setdefault("items", [])
        if item not in items:
            return "There is no such item here."
        items.remove(item)
        self.inventory.append(item)
        return f"You pick up the {item}."

    def _handle_inventory(self) -> str:
        if not self.inventory:
            return "You are empty-handed."
        return "You are carrying: " + ", ".join(self.inventory)


def main() -> None:
    """Entry point for running the game via the command line."""
    game = Game()
    print("Welcome to the mini text adventure! Type 'quit' to exit.")
    print(game.describe_location())
    while True:
        command = input("\n> ")
        response = game.process_command(command)
        print(response)
        if response == "Thanks for playing!":
            break


if __name__ == "__main__":
    main()
