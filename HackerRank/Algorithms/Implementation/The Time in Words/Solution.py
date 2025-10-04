# https://www.hackerrank.com/challenges/the-time-in-words/problem
# HackerRank: The Time in Words

NUMBERS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "quarter",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
    "twenty",
    "twenty one",
    "twenty two",
    "twenty three",
    "twenty four",
    "twenty five",
    "twenty six",
    "twenty seven",
    "twenty eight",
    "twenty nine",
    "half",
]


def time_in_words(h: int, m: int) -> str:
    """Phrase the time as o'clock, "past", or "to" using a fixed number-word table."""
    # Time: O(1)   Space: O(1)
    if m == 0:
        return f"{NUMBERS[h]} o' clock"
    if m <= 30:
        suffix = "" if m % 15 == 0 else (" minute" if m == 1 else " minutes")
        return f"{NUMBERS[m]}{suffix} past {NUMBERS[h]}"
    suffix = "" if m % 15 == 0 else " minutes"
    return f"{NUMBERS[30 - m % 30]}{suffix} to {NUMBERS[h + 1]}"


def test() -> None:
    assert time_in_words(5, 0) == "five o' clock"
    assert time_in_words(5, 1) == "one minute past five"
    assert time_in_words(5, 15) == "quarter past five"
    assert time_in_words(5, 30) == "half past five"
    assert time_in_words(5, 40) == "twenty minutes to six"
    assert time_in_words(5, 45) == "quarter to six"
    assert time_in_words(3, 27) == "twenty seven minutes past three"
