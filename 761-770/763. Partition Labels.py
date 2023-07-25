class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {}  # char -> [start, end]
        for i in range(len(s)):
            count[s[i]] = [count.get(s[i], [i, i])[0], i]

        sCount = list(count.values())
        sCount.sort()
        res = []
        curStart, curEnd = 0, 0
        for n in sCount:
            start, end = n
            if start >= curStart and end <= curEnd:
                continue
            elif start <= curEnd and end > curEnd:
                curEnd = end
            else:
                res.append(curEnd - curStart + 1)
                curStart = curEnd + 1
                curEnd = end
        res.append(curEnd - curStart + 1)

        return res
