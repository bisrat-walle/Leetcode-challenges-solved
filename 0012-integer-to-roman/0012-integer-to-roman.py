class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        
        ans = []
        
        for key in sorted(mapping, reverse=True):
            while num >= key:
                num -= key
                ans.append(mapping[key])
        return "".join(ans)