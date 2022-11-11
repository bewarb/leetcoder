class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d1 = {}
        for letter in t:
            d1[letter] = d1.get(letter, 0) + 1
        
        d2 = {}
        for letter in s:
            d2[letter] = d2.get(letter, 0) + 1
        
        for key, value in d1.items():
            if key not in d2 or d2[key] < d1[key]:
                return key
