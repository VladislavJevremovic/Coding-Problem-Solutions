// https://app.codility.com/programmers/lessons/92-tasks_from_indeed_prime_2016_college_coders_challenge/tennis_tournament/
// Effortless

public func solution(_ P : Int, _ C : Int) -> Int {
    return P > C * 2 ? C : P / 2
}