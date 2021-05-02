#%%
nums = [3,2,4]
target = 6
Output: [0,1]
#%%
nums = [3,2,4]
target = 6
##Output: [1,2]
#%%
nums = [3,3]
target = 6
##Output: [0,1]
#%%
ans = []
h = {}
for i, num in enumerate(nums):
    n = target - num
    if n not in h:
        h[num] = i
    else:
        ans = [h[n], i]
#%%
ans1 = []
inv_map = {v: k for k, v in dict(enumerate(nums)).items()}
for i, num in enumerate(nums):
    n = target - num
    if n in inv_map:
        ans1 = [inv_map[n], i]
#%%
##Way 1
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]