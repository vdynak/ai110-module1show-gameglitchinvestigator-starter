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

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
