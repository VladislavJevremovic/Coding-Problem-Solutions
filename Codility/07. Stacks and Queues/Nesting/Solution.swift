// https://app.codility.com/programmers/lessons/7-stacks_and_queues/nesting/
// Painless

public func solution(_ S : inout String) -> Int {
    var stack = [Character]()

    for c in S {
        if c == "(" {
            stack.append(c)
        } else {
            if stack.isEmpty {
                return 0
            }
            _ = stack.popLast()
        }
    }

    return stack.isEmpty ? 1 : 0
}