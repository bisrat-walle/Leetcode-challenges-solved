


class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        lcm = divisor1 * divisor2 // math.gcd(divisor1, divisor2)
        left, right = 2, 2 * 10**9
        while left < right:
            mid = (left+right)//2
            one = mid - mid//divisor1
            two = mid - mid//divisor2
            union = mid//divisor1 + mid//divisor2 - mid//lcm
            common = mid - union
            if one >= uniqueCnt1 and two >= uniqueCnt2 and one + two - common >= uniqueCnt1 + uniqueCnt2:
                right = mid
            else:
                left = mid+1
        return left
            