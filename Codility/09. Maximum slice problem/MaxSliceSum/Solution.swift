// https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_slice_sum/
// Painless

public func solution(_ A : inout [Int]) -> Int {
    var max_ending = -1_000_000
    var max_slice = -1_000_000
    
    for a in A {
        max_ending = max(a, max_ending + a)
        max_slice = max(max_slice, max_ending)
    }
    
    return max_slice
}