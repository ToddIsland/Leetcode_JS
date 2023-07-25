class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [0, 0, 0]
        for n in triplets:
            n1 = max(cur[0], n[0])
            n2 = max(cur[1], n[1])
            n3 = max(cur[2], n[2])
            if n1 <= target[0] and n2 <= target[1] and n3 <= target[2]:
                cur = [n1, n2, n3]
            if cur == target:
                return True

        return False
