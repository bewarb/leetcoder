class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n: str = str(abs(n))
        res = 0
        for i in range(len(n)):
            if i % 2 == 0:
                res = res + int(n[i])
            else:
               res = res - int(n[i])
        return res
        '''
        #Splits n into seperate numbers and into strings
        total = [str(int(digit)) for digit in str(n)]
        final = []

        for digit in range(len(total)):
        #every even number is +
            if (digit % 2) == 0:
                total[digit] =  int('+' + total[digit])
                print(total)
            else:
                #every odd is -
                total[digit] =  int('-' + total[digit])
        
        return sum(total)
        '''

                
        
