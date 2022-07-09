class Solution:
    def divisorGame(self, n: int) -> bool:
        '''
        n, t == (x) ==> n-x, t+1
        
        '''
        @lru_cache(None)
        def dp(n, turn=True):
            for x in range(1,n): # Possibilities
                if n%x==0: 
                    if dp(n-x, not turn): 
                        return True
                    else:
                        return False
            
            return turn == True

        return dp(n, 0)
                