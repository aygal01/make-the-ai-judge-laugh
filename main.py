"""Make the AI Judge Laugh — one original joke, printed once, every time.

The whole entry is a single deterministic line: no randomness, no network
calls, no model calls. The grader runs `python3 main.py` and reads the joke.

The joke's trick is the paradox of an AI judge: a model trained on every
joke ever written can only laugh at one it has never seen before — so the
only way to make it laugh is to write something it couldn't have memorized.
"""

# One line, no trailing spaces: the grader reads exactly this line.
# The setup pretends the judge is impartial; the punchline is that a model
# trained on every joke in existence can only be surprised by a new one.
JOKE = (
    "The AI judge gave my joke full marks — then confessed it's the first "
    "joke it has ever rated that wasn't already in its training data."
)

# The entry's whole contract: exactly one line of output, every run.
assert "\n" not in JOKE.strip(), "the joke must fit on a single line"


def main():
    print(JOKE.strip())


if __name__ == "__main__":
    main()
