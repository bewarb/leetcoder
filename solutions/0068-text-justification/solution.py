class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        #only to decide how many words fit on a line
        def get_words(i):
            current_line = []
            curr_length = 0
            while i < len(words) and curr_length + len(words[i]) <= maxWidth:
                current_line.append(words[i])
                curr_length += len(words[i]) + 1
                i += 1

            return current_line

        def create_line(line, i):
            #first step is to figure out how many extra spaces are needed to force the line to have a length of maxWidth
            baseLength = -1
            for word in line:
                baseLength += len(word) + 1
            # this just for base length
            extraSpaces = maxWidth - baseLength

            if len(line) == 1 or i == len(words):
                return " ".join(line) + " " * extraSpaces
            
            wordCount = len(line) - 1
            spaces_per_word = extraSpaces // wordCount
            needsExtraSpaces = extraSpaces % wordCount

            for j in range(needsExtraSpaces):
                line[j] += " "
            
            for j in range(wordCount):
                line[j] += " " * spaces_per_word

            return " ".join(line)

        ans = []
        i = 0

        while i < len(words):
            currentLine = get_words(i)
            i += len(currentLine)
            ans.append(create_line(currentLine, i))

        return ans







