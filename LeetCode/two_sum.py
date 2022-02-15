class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num in enumerate(nums):
            for j,num_ in enumerate(nums[i+1:]):
                if num+num_==target:
                    return [i,i+j+1]
        
