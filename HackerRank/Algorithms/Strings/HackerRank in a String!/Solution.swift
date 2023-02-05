func hackerrankInString(s: String) -> String {
    let mask = "hackerrank"
    var position = 0
    for c in s where position < mask.count {
        let searchIndex = mask.index(mask.startIndex, offsetBy: position)
        let searchCharacter = String(mask[searchIndex])
        if String(c) == searchCharacter {
            position += 1
        }
    }

    return position >= mask.count ? "YES" : "NO"
}