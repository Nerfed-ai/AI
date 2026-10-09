import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from game import Game


def test_take_item_and_move_between_rooms():
    game = Game()

    look = game.process_command("look")
    assert "forest clearing" in look
    assert "lantern" in look

    take = game.process_command("take lantern")
    assert take == "You pick up the lantern."
    assert "lantern" in game.inventory

    inventory = game.process_command("inventory")
    assert inventory == "You are carrying: lantern"

    move = game.process_command("go north")
    assert "cottage" in move
    assert game.location == "cottage"
