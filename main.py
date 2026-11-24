"""Office Jokes — Make the AI Judge Laugh.

Prints one original office one-liner, deterministically.
No input, no randomness, no network: the same line, every run.
"""

import sys

JOKE = (
    "I survived another meeting that could have been an email, "
    "and my reward was three more meetings about that email."
)


def get_joke() -> str:
    return JOKE


def main() -> int:
    print(get_joke())
    return 0


if __name__ == "__main__":
    sys.exit(main())
