import sys
import os

# add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import greet

def test_greet_success():
    assert greet("Kshithi") == "Hello, Kshithi"

def test_greet_empty():
    assert greet("") == "Hello, "

def test_greet_type():
    assert isinstance(greet("Test"), str)
