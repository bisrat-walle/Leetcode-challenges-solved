class Solution:
    def numberToWords(self, num: int) -> str:
        zero = 0
        if num == zero:
            return "Zero"
        
        mapping = {
            1000000000: "Billion",
            1000000: "Million",
            1000: "Thousand",
            100: "Hundred",
            90: "Ninety",
            80: "Eighty",
            70: "Seventy",
            60: "Sixty",
            50: "Fifty",
            40: "Forty",
            30: "Thirty",
            20: "Twenty",
            19: "Nineteen",
            18: "Eighteen",
            17: "Seventeen",
            16: "Sixteen",
            15: "Fifteen",
            14: "Fourteen",
            13: "Thirteen",
            12: "Twelve",
            11: "Eleven",
            10: "Ten",
            9: "Nine",
            8: "Eight",
            7: "Seven",
            6: "Six",
            5: "Five",
            4: "Four",
            3: "Three",
            2: "Two",
            1: "One",
            # 0: "Zero"
        }
        
        def rec(current_num):
            ans = []
            for key in sorted(mapping, reverse=True):
                if current_num >= key:
                    prefix = current_num//key
                    current_num = current_num%key
                    if prefix and key >= 100:
                        ans.append(rec(prefix))
                    ans.append(mapping[key])
                    if not current_num:
                        break
            return " ".join(ans)
        
        return rec(num)