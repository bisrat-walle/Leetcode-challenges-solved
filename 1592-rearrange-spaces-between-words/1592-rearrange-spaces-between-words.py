class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        spaces = 0
        for ch in text:
            if ch == " ":
                spaces += 1
        words = list(map(lambda a:a.strip(), text.split()))
        if len(words) == 1:
            return words[0] + " "*spaces
        number_of_spaces = spaces // (len(words)-1)
        space_counter = 0
        for index in range(len(words)-1):
            words[index] += " "*number_of_spaces
        an = "".join(words)
        an += " "*(len(text)-len(an))
        return an