# test_main.py
import main

def test_example():
    # Eenvoudige test om te kijken of pytest werkt
    assert 1 + 1 == 2

def test_no_secret_in_code():
    # Controleer dat de sleutel niet publiek is
    assert "supersecretkey123" not in main.secret_key
