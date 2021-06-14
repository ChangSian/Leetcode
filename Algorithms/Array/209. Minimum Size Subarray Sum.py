## EX1
target = 7
nums = [2,3,1,2,4,3]
## Output: 2
## Explanation: The subarray [4,3] has the minimal length under the problem constraint.


## EX2
target = 4
nums = [1,4,4]
## Output: 1

## EX3
target = 11
nums = [1,1,1,1,1,1,1,1]
## Output: 0


## 暴力解法(这道题目暴力解法当然是 两个for循环，然后不断的寻找符合条件的子序列，时间复杂度很明显是O(n^2)。)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        size = len(nums)
        if (1 <= target) & (target <= 10**9) & (1 <= size) & (size <= 10**5):            
        
            result = int(size+1)
            for i in range(size):
                sum = 0
                for j in range(i, size):
                    sum = sum + nums[j]

                    if (sum >= target):
                        subsize = j-i+1

                        if (subsize < result):
                            result = subsize
                        break

            if result > size:
                return 0
            else:
                return result
        else:
            return 0

## 滑动窗口(滑动窗口的精妙之处在于根据当前子序列和大小的情况，不断调节子序列的起始位置。从而将O(n^2)的暴力解法降为O(n)。)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = int(len(nums)+1)
        sum = 0
        start = 0
        size = len(nums)

        for end in range(len(nums)):
            sum = sum + nums[end]
            while (sum >= target):
                size = end - start + 1
                sum = sum - nums[start]
                start  = start +1 
    
                if size < result:
                    result = size

        if result > len(nums):
            return 0
        else:
            return result
