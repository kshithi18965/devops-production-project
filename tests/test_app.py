from main import greet

def test_greet_success():
    assert greet("Kshithi") == "Hello, Kshithi"

def test_greet_empty():
    assert greet("") == "Hello, "

def test_greet_type():
    assert isinstance(greet("Test"), str)
