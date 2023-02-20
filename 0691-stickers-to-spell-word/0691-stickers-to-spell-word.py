class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        sticker_counts = [Counter(s) for s in stickers]
        target_count = Counter(target)
        n = len(target)

        @lru_cache(maxsize=None)
        def dp(subseq_count):
            if all(subseq_count[i] == 0 for i in range(n)):
                return 0

            ans = float("inf")
            for sticker_count in sticker_counts:
                new_count = tuple(max(subseq_count[i] - sticker_count[target[i]], 0) for i in range(n))
                if new_count != subseq_count:
                    ans = min(ans, 1 + dp(new_count))

            return ans

        ans = dp(tuple(target_count[c] for c in target))
        return ans if ans < float("inf") else -1
