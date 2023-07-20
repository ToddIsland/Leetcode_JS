class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":return ""
        res, resLen = [-1, -1], float("inf")
        window, countT = {}, {}

        for i in t:
            countT[i] = 1 + countT.get(i, 0)

        have, need = 0, len(countT)

        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in countT and countT[s[r]] == window[s[r]]:
                have += 1

            while need == have:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                # remember increment l cuz we move l forward
                l += 1
        l, r = res

        return s[l : r + 1] if resLen != float("inf") else ""
