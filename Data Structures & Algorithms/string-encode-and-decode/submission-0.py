class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            # Find the delimiter '#'
            j = i
            #print("j: ", j)
            while s[j] != "#":
                j += 1
                #print("j: ", j)
            length = int(s[i:j])  # Length of the string
            #print("length: ", length)
            i = j + 1  # Move past '#'
            #print("i: ", i)
            decoded.append(s[i:i+length])  # Extract the actual string
            #print("decoded: ", decoded)
            i += length  # Move to the next encoded part
        return decoded
