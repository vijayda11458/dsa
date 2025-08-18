class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cur = sum(cardPoints[:k]); 
        best = cur
        for i in range(1, k+1):
            cur = cur - cardPoints[k-i] + cardPoints[-i]
            if cur > best: best = cur
        return best
        
        