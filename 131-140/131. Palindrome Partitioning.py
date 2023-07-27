class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def iter(i):
            if i == len(s):
                res.append(part[:])
                return
            for j in range(i, len(s)):
                if self.Palin(s, i, j):
                    part.append(s[i : j + 1])
                    iter(j + 1)
                    part.pop()

        iter(0)

        return res

    def Palin(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
