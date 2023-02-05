# https://leetcode.com/problems/encode-and-decode-tinyurl

class Codec:
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
