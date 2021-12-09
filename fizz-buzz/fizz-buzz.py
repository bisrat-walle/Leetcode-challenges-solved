class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        an = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                an.append("FizzBuzz")
            elif i % 3 == 0:
                an.append("Fizz")
            elif i % 5 == 0:
                an.append("Buzz")
            else:
                an.append(str(i))
        return an