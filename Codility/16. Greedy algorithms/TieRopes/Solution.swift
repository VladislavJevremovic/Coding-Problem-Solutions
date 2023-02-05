// https://app.codility.com/programmers/lessons/16-greedy_algorithms/tie_ropes/
// Painless

public func solution(_ K : Int, _ A : inout [Int]) -> Int {
    var count = 0
    var current = 0
    
    for R in A {
        current += R
        if current >= K {
            count += 1
            current = 0
        }
    }
    
    return count
}