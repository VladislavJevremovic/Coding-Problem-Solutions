// https://app.codility.com/programmers/lessons/99-future_training/tree_height/
// Painless

public func solution(_ T : Tree?) -> Int {
    guard let T = T else {
        return -1
    }
    
    return max(solution(T.l), solution(T.r)) + 1
}