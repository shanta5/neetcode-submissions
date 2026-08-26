class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            for i in s:
                index = t.find(i)
                if index != -1:  # Check if the letter exists
                    t = t[:index] + t[index+1:]
                    if not t:
                        return True
            return False 
        