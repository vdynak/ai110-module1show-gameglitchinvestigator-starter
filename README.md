# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

### What's the game about?
It's a number guessing game built with Streamlit where you try to guess a randomly-generated secret number within a difficulty range. You get hints and a score, and the game's supposed to tell you whether to guess higher or lower. Pretty straightforward, but the AI that built it... yeah, didn't really nail it.

### Bugs we found
The AI left us with a couple of rough ones. First, the directional hints were completely backwards — if your guess was too high, it'd tell you to go higher instead of lower. Super confusing when you're trying to actually win. Second, the game was letting people spam guesses outside the valid range without penalty, which felt like cheating. And the test cases weren't even checking the full return values, so we wouldn't have caught these problems if we hadn't actually run them.

### What we fixed
We moved the `check_guess()` function out of the main app file and into `logic_utils.py` where it belongs, then swapped the emoji and messages so the hints actually make sense now. Added proper range validation too — now if you try to guess outside the difficulty range, it tells you no and doesn't waste one of your attempts. Fixed the tests to actually unpack and verify both the outcome and the message, then wrote a specific test case to make sure the high/low bug doesn't come back. All tests pass now, so we're good.

## 📸 Demo

<img width="1171" height="647" alt="Screenshot 2026-03-02 at 11 55 19 AM" src="https://github.com/user-attachments/assets/c37cc784-0da0-4fc6-9e88-b01e8b10d0dd" />

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]

---

## 📋 Project Review – June 2026

### What the project does
This project is a fully-functional number guessing game built with Streamlit. Players select a difficulty level (Easy: 1-20, Normal: 1-100, Hard: 1-50), receive hints that correctly guide them whether to guess higher or lower, and earn points based on how quickly they find the secret number. It's a hands-on demonstration of debugging AI-generated code, understanding Streamlit's session state management, and implementing proper testing practices.

### Bugs that were fixed
- **High/Low hint directions were backwards**: The game said "Go HIGHER" when the guess was too high, and vice versa. Fixed by correcting the conditional logic and message pairings in `check_guess()`.
- **Secret number changed on every button click**: Streamlit was re-running the entire script without preserving the secret number. Fixed by using `st.session_state` to persist the value across reruns.
- **Out-of-range guesses weren't validated**: Players could guess outside the difficulty range and still use up an attempt. Added proper range checking before incrementing the attempt counter.
- **Test cases weren't comprehensive**: Initial tests only checked outcome strings, not the full return tuples. Refactored tests to validate both outcome and hint message.

### What was learned
- **Streamlit's reactive execution model**: Every button click or text input triggers a complete re-run of the script from top to bottom. Session state is critical for persisting variables across these reruns.
- **The importance of testing**: Writing explicit test cases (especially `test_high_low_directions_bug_fix`) caught subtle logic errors that manual testing alone might have missed.
- **AI assistance has limits**: GitHub Copilot made several helpful suggestions (refactoring, identifying the high/low bug), but incomplete test stubs needed manual correction before they actually worked.
- **Code quality matters**: Moving logic into `logic_utils.py` made the code testable and maintainable, separating UI concerns from game logic.
