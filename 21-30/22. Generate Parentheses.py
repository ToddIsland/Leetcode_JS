class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        # str: current string
        # left: amount of left brackets
        # remain: amount of remain left brackets
        def iter(str, left):
            if len(str) == 2 * n:
                if left == 0: res.append(str)
                return
            if left > 0:
                iter(str + "(", left + 1)
                iter(str + ")", left - 1)
            else:
                iter(str + "(", left + 1)

        iter('', 0)

        return res