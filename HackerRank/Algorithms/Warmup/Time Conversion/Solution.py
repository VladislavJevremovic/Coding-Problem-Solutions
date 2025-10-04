# https://www.hackerrank.com/challenges/time-conversion/problem
# HackerRank: Time Conversion


def time_conversion(s: str) -> str:
    """Convert a 12-hour AM/PM time (hh:mm:ssAM) to 24-hour format (HH:mm:ss)."""
    # Time: O(1)   Space: O(1)
    period = s[-2:]
    hour = int(s[:2])
    rest = s[2:-2]
    if period == "AM":
        hour = 0 if hour == 12 else hour
    else:  # PM
        hour = 12 if hour == 12 else hour + 12
    return f"{hour:02d}{rest}"


def test() -> None:
    assert time_conversion("07:05:45PM") == "19:05:45"
    assert time_conversion("12:00:00AM") == "00:00:00"
    assert time_conversion("12:00:00PM") == "12:00:00"
    assert time_conversion("01:23:45AM") == "01:23:45"
