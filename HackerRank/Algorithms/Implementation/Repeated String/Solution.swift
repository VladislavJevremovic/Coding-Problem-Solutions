extension String {
    var aCount: Int {
        return filter { $0 == "a" }.count
    }
}

func repeatedString(s: String, n: Int) -> Int {
    if n < s.count {
        return String(s.prefix(s.count - n + 1)).aCount
    } else {
        return s.aCount * (n / s.count) + String(s.prefix(n % s.count)).aCount
    }
}
