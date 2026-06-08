from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_high_low_directions_bug_fix():
    # FIX: Created test case with Copilot Agent mode to validate the high/low direction bug fix
    """
    Test that high/low messages are correct.
    
    Bug: The emoji and direction hints were swapped.
    - When guess > secret (too high), message should say "Go LOWER!" with 📉
    - When guess < secret (too low), message should say "Go HIGHER!" with 📈
    """
    # Test: guess is too high
    outcome_high, message_high = check_guess(75, 50)
    assert outcome_high == "Too High"
    assert message_high == "📉 Go LOWER!"
    
    # Test: guess is too low
    outcome_low, message_low = check_guess(25, 50)
    assert outcome_low == "Too Low"
    assert message_low == "📈 Go HIGHER!"


def test_boundary_values():
    """Test edge cases: extreme low and extreme high guesses."""
    # Very low guess
    outcome, message = check_guess(1, 100)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"
    
    # Very high guess
    outcome, message = check_guess(1000, 100)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_string_type_handling():
    """Test that check_guess handles string secrets (edge case from session state)."""
    # String comparison fallback when secret is stored as string
    outcome, message = check_guess(75, "50")
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"
    
    outcome, message = check_guess(25, "50")
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_multiple_win_scenarios():
    """Test winning at different difficulty ranges."""
    # Easy difficulty: win in range 1-20
    outcome, message = check_guess(15, 15)
    assert outcome == "Win"
    assert message == "🎉 Correct!"
    
    # Hard difficulty: win in range 1-50
    outcome, message = check_guess(42, 42)
    assert outcome == "Win"
    assert message == "🎉 Correct!"
    
    # Normal difficulty: win in range 1-100
    outcome, message = check_guess(87, 87)
    assert outcome == "Win"
    assert message == "🎉 Correct!"