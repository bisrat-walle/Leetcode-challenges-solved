class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        def all_are_a(st):
            all_a = True
        
            for i in st:
                if i != "a":
                    all_a = False
                    break
            return all_a
        
        all_a = all_are_a(palindrome)
        
        for i in palindrome:
            if i != "a":
                all_a = False
                break
        
        if all_a:
            an = ""
            for i in palindrome[:-1]:
                an += i
            an += "b"
        else:
            for i in range(len(palindrome)):
                if palindrome[i] != "a":
                    index = i
                    break
            an = palindrome[:index] + "a" + palindrome[index+1:]
        if all_are_a(an):
            an = palindrome[:-1] +  "b"
        
        return an