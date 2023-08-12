# https://leetcode.com/problems/encode-and-decode-tinyurl/

class Codec:
    def __init__(self):
        self.encodeMap = {}
        self.decodeMap = {}
        self.base = 'http://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        short = self.base + str(len(self.encodeMap) + 1)
        self.encodeMap[longUrl] = short
        self.decodeMap[short] = longUrl

        return short

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """

        return self.decodeMap[shortUrl]