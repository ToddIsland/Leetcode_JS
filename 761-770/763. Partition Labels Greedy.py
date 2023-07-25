class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {}  # char -> lastIndex
        for i in range(len(s)):
            count[s[i]] = i

        index = 0
        curLen = 0
        res = []

        for i in range(len(s)):
            index = max(index, count[s[i]])
            curLen += 1

            if i == index:
                res.append(curLen)
                curLen = 0

        return res
