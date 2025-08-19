from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        pCount = Counter(p)
        sCount = Counter()
        k = len(p)

        for i, ch in enumerate(s):
        # add new char to window
            sCount[ch] += 1

        # remove char if window > k
            if i >= k:
                left_char = s[i - k]
                sCount[left_char] -= 1
                if sCount[left_char] == 0:
                    del sCount[left_char]

        # check match
            if sCount == pCount:
                res.append(i - k + 1)

        return res