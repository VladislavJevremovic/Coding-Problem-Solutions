func matchingStrings(strings: [String], queries: [String]) -> [Int] {
    return queries.compactMap {
        let query = $0
        return strings.filter {$0 == query}.count
    }
}