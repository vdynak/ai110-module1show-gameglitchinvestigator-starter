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

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
