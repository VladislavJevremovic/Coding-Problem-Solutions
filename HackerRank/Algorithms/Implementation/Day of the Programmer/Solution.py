# https://www.hackerrank.com/challenges/day-of-the-programmer/problem
# HackerRank: Day of the Programmer
def day_of_programmer(year: int) -> str:
    """Locate the 256th day by branching on Julian/Gregorian/1918-transition rules."""
    # Time: O(1)   Space: O(1)
    if year == 1918:
        # Transition year: 1..13 Feb were skipped, shifting the 256th day.
        return "26.09.1918"

    if year < 1918:
        leap = year % 4 == 0  # Julian calendar
    else:
        leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)  # Gregorian

    day = 12 if leap else 13
    return f"{day:02d}.09.{year}"


def test() -> None:
    assert day_of_programmer(2017) == "13.09.2017"
    assert day_of_programmer(2016) == "12.09.2016"  # Gregorian leap year
    assert day_of_programmer(1918) == "26.09.1918"  # transition year
    assert day_of_programmer(1800) == "12.09.1800"  # Julian leap (1800 % 4 == 0)
