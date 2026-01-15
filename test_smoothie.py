import sys
from pathlib import Path
from smoothie import smoothie
sys.path.append(str(Path(__file__).parent.parent / "src"))


def test_smoothie():
    assert smoothie(["banana", "strawberry", "yogurt"]) == "Icy Water smoothie with banana, strawberry, yogurt"
    assert smoothie(["berries"]) == "Icy Water smoothie with berries"
    assert smoothie(["1","2","3"]) == "Icy Water smoothie with 1, 2, 3"  
    assert smoothie([]) == "Icy Water!"
    assert smoothie(["banana", "strawberry", "yogurt"],"",False) == "Water smoothie with banana, strawberry, yogurt"
    assert smoothie([],"", False ) == "Just Water!"
    assert smoothie(["kiwi", "banana", "cherry"], "", False)
    #...  # Continue adding tests here


print(test_smoothie())