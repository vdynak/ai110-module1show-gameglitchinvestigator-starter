def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty.
    
    Args:
        difficulty: One of "Easy", "Normal", or "Hard".
        
    Returns:
        A tuple (low, high) representing the inclusive number range.
        Default range is 1-100 if difficulty is not recognized.
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """Parse user input into an integer guess with validation.
    
    Attempts to convert the input string to an integer, handling decimal
    notation (e.g., "5.0" -> 5). Returns success/failure with error messaging.

    Args:
        raw: Raw string input from the user.
        
    Returns:
        Tuple of (ok: bool, guess_int: int | None, error_message: str | None)
        - If parsing succeeds, returns (True, int_value, None)
        - If parsing fails, returns (False, None, error_description)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """Compare a player's guess against the secret number and return feedback.
    
    This function handles the core game logic: determining if the guess is correct,
    too high, or too low. It gracefully handles type mismatches by converting to
    strings when necessary (important for Streamlit's session state edge cases).
    
    BUG FIX (June 2026): Fixed high/low direction logic. Previously returned
    "📈 Go HIGHER!" when guess > secret, which was backwards. Now correctly returns
    "📉 Go LOWER!" for guesses that exceed the secret, and vice versa.

    Args:
        guess: The player's current guess (int or str).
        secret: The secret number to match (int or str).
        
    Returns:
        Tuple of (outcome: str, message: str) where:
        - outcome is one of: "Win", "Too High", "Too Low"
        - message is a player-friendly hint with emoji guidance
    """
    # FIX: Refactored from app.py and fixed high/low direction bug with Copilot Agent mode.
    # Bug was: "Go HIGHER!" when guess > secret (backwards). Now correctly shows "Go LOWER!"
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        # Handle string comparison fallback for edge cases
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Calculate score changes based on game outcome and attempt number.
    
    Scoring rules:
    - Win: Earn 100 - (10 * attempts) points, minimum 10 points
    - Too High: Bonus 5 points on even attempts, lose 5 on odd attempts
    - Too Low: Lose 5 points
    
    Args:
        current_score: The player's current score before this outcome.
        outcome: One of "Win", "Too High", "Too Low".
        attempt_number: Which attempt this is (0-indexed).
        
    Returns:
        Updated score after applying outcome-based changes.
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
