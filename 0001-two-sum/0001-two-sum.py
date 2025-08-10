class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result =[]
        mapData = {}
        for i in range(len(nums)):
            if target-nums[i] in mapData:
                return [i,mapData.get(target-nums[i])]
            else:
                mapData[nums[i]] = i
        return result


        