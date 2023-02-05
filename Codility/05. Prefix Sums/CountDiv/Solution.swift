// https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/
// Respectable

public func solution(_ A : Int, _ B : Int, _ K : Int) -> Int {
    if A > B || K < 1 {
        return 0
    }
    
    let start = ((A + (K - 1)) / K) * K
    if start > B {
        return 0
    }
    
    return 1 + (B - start) / K
}