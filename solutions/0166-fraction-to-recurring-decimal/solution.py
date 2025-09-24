class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        result = []

        if numerator == 0:
            return "0"
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        
        num,den = abs(numerator), abs(denominator)
        #How many times it goes into the number
        result.append(str(num//den))
        num %= den

        if num == 0:
            return "".join(result)
        
        #Fractions
        result.append(".")
        remain_pos = {}
        #dict to 

        while num:
            if num in remain_pos:
                pos = remain_pos[num]
                result.insert(pos,"(")
                result.append(")")
                break
            
            remain_pos[num] = len(result)
            num *= 10
            result.append(str(num // den))
            num %= den
        
        return "".join(result)

        
