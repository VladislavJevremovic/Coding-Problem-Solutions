# https://leetcode.com/problems/encode-and-decode-tinyurl


class Codec:
    """Store each long URL under the hash of itself and look it back up on
    decode.

    encode: Time O(n)   Space O(n)   (n = URL length)
    decode: Time O(1)   Space O(1)
    """

    def __init__(self):
        self.d = {}

    def encode(self, longUrl):
        h = hash(longUrl)
        self.d[h] = longUrl
        return h

    def decode(self, shortUrl):
        return self.d[shortUrl]


def test():
    c = Codec()
    url = "https://leetcode.com/problems/design-tinyurl"
    assert c.decode(c.encode(url)) == url
