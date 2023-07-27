class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []
        pMap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        res = []
        string = ""

        def iter(i):
            nonlocal string
            if i == len(digits):
                res.append(string)
                return
            chars = pMap[digits[i]]
            for c in chars:
                string += c
                iter(i + 1)
                string = string[:-1]

        iter(0)
        return res
