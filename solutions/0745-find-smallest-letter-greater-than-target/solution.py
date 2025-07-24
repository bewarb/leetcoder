class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)

        #lower bound
        while l < r:
            m = (l + r) // 2
            if letters[m] > target:
                r = m   
            else:
                l = m + 1  # go right

        if l < len(letters):
            return letters[l]
        else:
            return letters[0]



        
