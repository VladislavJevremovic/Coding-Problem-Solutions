# https://app.codility.com/programmers/lessons/92-tasks_from_indeed_prime_2016_college_coders_challenge/tennis_tournament/
# Effortless


def solution(P: int, C: int) -> int:
    """Each match needs two players and one court, so cap the pairings by whichever resource runs out first."""
    # Time: O(1)   Space: O(1)
    return C if P > C * 2 else P // 2


def test() -> None:
    assert solution(5, 3) == 2
    assert solution(10, 3) == 3
    assert solution(0, 5) == 0
    assert solution(8, 4) == 4
