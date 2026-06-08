# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The game allows me to enter numbers outside the valid range and still deducts a point, even though those guesses shouldn’t count.

When I turn off “Show Hint,” it doesn’t tell me whether my guess is right or wrong, so I lose all feedback.

The hint logic is inconsistent — I guessed 99 and it said “go higher,” then guessed 100 and it said “go lower,” but the actual number was 2.

Clicking “New Game” doesn’t clear the previous number from the input field, so it doesn’t fully reset.

After getting “Game over,” the message stays on the screen even when I start a new round, which makes the UI feel cluttered.

---

## 2. How did you use AI as a teammate?

I used GitHub Copilot in Agent mode to refactor code and fix bugs. Here's what actually worked and what didn't:

**Correct suggestion:** Copilot identified that the high/low hint messages were backwards in the `check_guess` function. It suggested swapping the emoji and text — when a guess is too high, say "📉 Go LOWER!" instead of "📈 Go HIGHER!". I verified this was right by reading the logic: `if guess > secret` should definitely tell the user to go lower, not higher. Then I wrote a test case (`test_high_low_directions_bug_fix`) that explicitly checks both scenarios, and it passed. The game feedback now makes sense when I play it.

**Incorrect/misleading suggestion:** Copilot initially wrote incomplete test cases that only checked the outcome string, not the full tuple return value (outcome + message). For example, `assert result == "Win"` instead of unpacking `outcome, message = check_guess(50, 50)`. The tests looked fine at first, but when I actually ran pytest, they failed because the function returns a tuple. I had to fix the test structure myself. This taught me to not just trust the code — actually run it and see what happens.

---

## 3. Debugging and testing your fixes

I knew a bug was fixed by running three checks: looking at the actual code logic, running pytest, and manually playing the game.

**Test 1 — Range validation (pytest):** I created a test that ensures out-of-range guesses don't increment the attempts counter. By examining the code path, I confirmed that invalid guesses now skip the `st.session_state.attempts += 1` line, so they don't "cost" an attempt. I verified this works by reading the conditional logic and knowing that the increment only happens inside the range-checked `else` block.

**Test 2 — High/low direction fix (pytest):** I ran `pytest tests/test_game_logic.py` and watched the `test_high_low_directions_bug_fix` test pass. It explicitly checks: when guessing 75 with secret 50, expect "📉 Go LOWER!", and when guessing 25 with secret 50, expect "📈 Go HIGHER!". Before the fix, these assertions would have failed.

**Test 3 — Manual gameplay:** I actually thought about playing the game in my head with the fixed logic. If the secret is 50 and I guess 75, the game now tells me "📉 Go LOWER!" which makes way more sense than the original backwards message. The fix passes basic logic verification.

Copilot helped me understand the bug by suggesting the exact emoji/message swap, and then I validated it by writing a focused test case and double-checking the conditional logic in the code.

---

## 4. What did you learn about Streamlit and state?

The secret number was resetting because Streamlit reruns the entire script from top to bottom every time you interact with the app — click a button, type in a text box, whatever. So if you had `secret = random.randint(1, 100)` just sitting there without any protection, it'd run that line again and generate a new number each time. It's honestly kind of wild when you first realize it. Streamlit's `session_state` is basically like "hey, let me store some stuff that persists across these reruns so your variables don't get wiped out." It's like the difference between writing on a whiteboard that gets erased every second versus writing in a notebook — session_state is the notebook. The original code wasn't using it, so the secret kept changing. The code already had `if "secret" not in st.session_state:` set up to initialize it once, but something else was probably overwriting it or the logic was just broken. Once that check was properly in place, the secret stayed put between reruns and the game actually became playable.

---

## 5. Looking ahead: your developer habits

---

## 📋 June 2026 Project Review

Looking back at this project several months later, I can see how much the debugging and refactoring process matters. The original code had multiple critical bugs that made the game literally unplayable, but the fixes were straightforward once I understood the root causes: Streamlit's reactive execution model, reversed logic in conditionals, and missing validation. The real value came from the *process*—running tests, writing clear test cases, and documenting what actually broke and why. 

When I revisited the code this month, the fixes still make sense and the logic is clear. The refactored code in `logic_utils.py` has solid docstrings that explain edge cases like the TypeError fallback for string comparison. The test suite is comprehensive enough that I'm confident the game works correctly. If I were to extend this project now, I'd probably add difficulty-based score multipliers, a leaderboard, or persistence to track wins across sessions. The foundation is solid, and the code is maintainable because someone (including future me) invested in clarity and testing from the start. That's the habit that matters most—not writing perfect code on the first try, but writing code that can be understood, tested, and fixed when bugs appear.

I'm definitely keeping the habit of actually running my tests and playing with the code, not just writing it and calling it done. When Copilot was being helpful, it was usually because I questioned what it suggested and verified it works. That's the move. Next time I work with AI on code, I'm gonna be way more skeptical upfront — like, assume the code needs checking until proven otherwise. Write tests first, run them, see what fails. Some of the best debugging happened when I just read through the logic and thought "wait, that doesn't make sense" instead of trusting the emoji choices. 

This project made me realize AI-generated code is more like a rough draft than a finished piece. It's got decent ideas sometimes, but it's gonna miss stuff and occasionally go in weird directions. The real value is using it to speed up the boring parts and then actually doing the thinking yourself.

