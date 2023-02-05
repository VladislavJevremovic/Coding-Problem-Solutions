let numbers: [String] = ["zero",  "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine", "half"];

// Complete the timeInWords function below.
func timeInWords(h: Int, m: Int) -> String {
    switch m {
    case 0:
        return "\(numbers[h]) o' clock"
    case 1...30:
        return "\(numbers[m])\(m % 15 == 0 ? "" : (m == 1 ? " minute" : " minutes")) past \(numbers[h])"
    default:
        return "\(numbers[30 - m % 30])\(m % 15 == 0 ? "" : " minutes") to \(numbers[h + 1])"
    }
}
