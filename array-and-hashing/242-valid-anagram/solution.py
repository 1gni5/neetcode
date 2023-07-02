class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0] * 26
        offset = ord('a')

        if len(s) != len(t):
            return False

        # register available letters
        for letter in s:
            counts[ord(letter) - offset] += 1

        # check if second word match conditions
        for letter in t:
            index = ord(letter) - offset
            counts[index] -= 1 # consume letter
            if counts[index] < 0:
                return False
            
        return True
