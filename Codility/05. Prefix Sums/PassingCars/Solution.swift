// https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/
// Painless

public func solution(_ A : inout [Int]) -> Int {
    var count = 0
    var pairs = 0

    for a in A {
        if a == 0 {
            count += 1
        } else {
            pairs += count
        }

        if pairs > 1_000_000_000 {
            return -1
        }
    }

    return pairs
}