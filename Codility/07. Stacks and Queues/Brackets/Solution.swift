// https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/
// Painless

public func solution(_ S : inout String) -> Int {
    func isMatchingPair(_ A : Character, _ B : Character) -> Bool {
        return (A == "(" && B == ")") || (A == "[" && B == "]") || (A == "{" && B == "}")
    }

    var stack = [Character]()

    for c in S {
        if c == "(" || c == "[" || c == "{" {
            stack.append(c)
        } else {
            if stack.isEmpty {
                return 0
            }

            if !isMatchingPair(stack.popLast()!, c) {
                return 0
            }
        }
    }

    return stack.isEmpty ? 1 : 0
}