class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        x = ""
        for c in s:
            if c.isalpha() or c.isnumeric():
                x += c

        i, j = 0, len(x) - 1
        while i <= j:
            if x[i] == x[j]:
                i += 1
                j -= 1
            else:
                return False

        return True
