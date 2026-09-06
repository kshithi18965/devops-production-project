import sys
import os

# add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import greet


def test_greet():
    # just check function runs without error
    assert greet() is None
