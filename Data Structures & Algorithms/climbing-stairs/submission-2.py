class Solution:
    cache = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
    }

    def climbStairs(self, n: int) -> int:
        # 0: 0
        # 1: 1
        #   1
        # 2: 2
        #   1 1
        #   2
        # 3: 3
        #   1 1 1
        #   1 2
        #   2 1
        # 4: 5
        #   1 1 1 1
        #   1 1 2
        #   1 2 1
        #   2 1 1
        #   2 2
        # 5: 8
        #   1 1 1 1 1
        #   1 1 1 2
        #   1 1 2 1
        #   1 2 1 1
        #   2 1 1 1
        #   1 2 2
        #   2 1 2
        #   2 2 1
        if n <= 3:
            return n
        if n in self.cache:
            return self.cache[n]
        result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.cache[n] = result
        return result