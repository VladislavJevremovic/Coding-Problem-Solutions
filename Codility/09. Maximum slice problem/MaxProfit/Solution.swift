// https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_profit/
// Painless

public func solution(_ A : inout [Int]) -> Int {
    var max_profit = 0
    var min_value = 200_000
    
    for day in A {
        min_value = min(min_value, day)
        max_profit = max(max_profit, day - min_value)
    }
    
    return max_profit
}