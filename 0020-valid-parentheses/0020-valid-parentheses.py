class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        dic={
            '(':')',
            '[':']',
            '{':'}'
        }
        for i in s:
            if i in dic:
                arr.append(dic[i])
            else:
                 if not arr or arr.pop() != i:
                    return False
        return not arr