class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        an = []
        index = 0
        while index < len(words):
            current_line = words[index]
            while index+1 < len(words):
                if len(current_line)+len(words[index+1])+1 > maxWidth:
                    break
                current_line += " " + words[index+1]
                index += 1
            temp_words = current_line.split()
            if len(temp_words) != 1:
                space_left = maxWidth - len(current_line)
                counter = 0
                temp_index = 0
                while counter < space_left:
                    temp_words[temp_index] += " "
                    counter += 1
                    temp_index = (temp_index+1)%(len(temp_words)-1)
            else:
                temp_words[0] += " "*(maxWidth-len(temp_words[0]))
            
            an.append(" ".join(temp_words))
            index += 1
        
        last_line = an[-1].split()
        last_line = " ".join(last_line)
        last_line += " "*(maxWidth-len(last_line))
        an[-1] = last_line
        
        
        return an