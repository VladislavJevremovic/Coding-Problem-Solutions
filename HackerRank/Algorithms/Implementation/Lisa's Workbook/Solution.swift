func workbook(n: Int, k: Int, arr: [Int]) -> Int {
    var numberOfSpecialProblems = 0
    var pageCount = 0
    for chapterProblemCount in arr {
        let chapterPageCount = chapterProblemCount / k

        for page in 0..<chapterPageCount {
            pageCount += 1
            if page * k + 1...(page + 1) * k ~= pageCount {
                numberOfSpecialProblems += 1
            }
        }

        let lastPageProblemCount = chapterProblemCount % k
        if lastPageProblemCount > 0 {
            pageCount += 1
            if chapterPageCount * k + 1...chapterProblemCount ~= pageCount {
                numberOfSpecialProblems += 1
            }
        }
    }

    return numberOfSpecialProblems
}