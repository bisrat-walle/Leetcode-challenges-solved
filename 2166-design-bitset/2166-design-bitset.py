class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.ons = set()
        self.flipped = False

    def fix(self, idx: int) -> None:
        self.ons.discard(idx) if self.flipped else self.ons.add(idx)

    def unfix(self, idx: int) -> None:
        self.ons.add(idx) if self.flipped else self.ons.discard(idx)

    def flip(self) -> None:
        self.flipped = not self.flipped
        

    def all(self) -> bool:
        return len(self.ons) == self.size if not self.flipped else \
                (self.size-len(self.ons)) == self.size 

    def one(self) -> bool:
        return len(self.ons) > 0 if not self.flipped else (self.size-len(self.ons)) > 0

    def count(self) -> int:
        return len(self.ons) if not self.flipped else self.size-len(self.ons)

    def toString(self) -> str:
        ans = [0]*self.size
        for index in range(len(ans)):
            ans[index] = str(int((
                ((index in self.ons) and not self.flipped)) or 
                ((index not in self.ons) and self.flipped))
            )
        return "".join(ans)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()