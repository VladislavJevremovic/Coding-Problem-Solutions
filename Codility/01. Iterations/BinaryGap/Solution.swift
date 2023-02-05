// https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
// Painless

import XCTest

public func solution(_ N : Int) -> Int {
    var maxGap = 0, gap = 0, gapOpen = false, n = N
    while n > 0 {
        let d = n % 2
        if d == 0 {
            if gapOpen {
                gap += 1
            }
        } else {
            gapOpen = true
            maxGap = max(maxGap, gap)
            gap = 0
        }

        n /= 2
    }

    return maxGap
}

class Tests: XCTestCase {
    func testSolution() {
        XCTAssertEqual(solution(1041), 5)
        XCTAssertEqual(solution(32), 0)
        XCTAssertEqual(solution(9), 2)
        XCTAssertEqual(solution(529), 4)
        XCTAssertEqual(solution(20), 1)
        XCTAssertEqual(solution(15), 0)
    }
}

Tests.defaultTestSuite.run()
