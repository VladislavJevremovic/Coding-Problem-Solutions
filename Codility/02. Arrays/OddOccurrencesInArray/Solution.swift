// https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
// Painless

public func solution(_ A : inout [Int]) -> Int {
    var s = Set<Int>()
    for i in A {
        if s.contains(i) {
            s.remove(i)
        } else {
            s.insert(i)
        }
    }

    return s.first!
}