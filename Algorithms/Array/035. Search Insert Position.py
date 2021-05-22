# WAY 1: 暴力破解

class Solution(object):
    def searchInsert(self, nums: List[int], target: int):
        
        if target in nums:
          index = nums.index(target)
        else:
          i= len(nums)-1
          while target - nums[i] <= 0 and i>=0:      
            i -=1
          index = i + 1

        return index

# WAY 2: Binary Search
##Target 位在左閉右閉區間


class Solution(object):
    def searchInsert(self, nums: List[int], target: int):
        
        n = len(nums)
        left  = 0
        right = n-1 ##定义target在左闭右闭的区间里，[left, right]

        while (left <= right ): ##當left == right, 區間[left, right] 依然有效
            middle = int(left + ((right - left)/2)) ## 防止溢出，等同於(left + right) / 2
            if (nums[middle] > target):
                right = middle - 1 ## Target 在左區間，所以[left, middle - 1]
            elif (nums[middle] < target):
                left = middle + 1 ## Target 在右區間，所以[middle+1, right]
            else: ## nums[middle] == target
                return middle 
          
        ## 分别处理如下四种情况
        ## 目标值在数组所有元素之前  [0, -1] 
        ## 目标值等于数组中某一个元素  return middle;
        ## 目标值插入数组中的位置 [left, right]，return  right + 1
        ## 目标值在数组所有元素之后的情况 [left, right]， return right + 1

        return right + 1


##Target 位在左闭右开區間

class Solution(object):
    def searchInsert(self, nums: List[int], target: int):
        
        n = len(nums)
        left  = 0
        right = n ##定义target在左闭右开的区间里，[left, right)

        while (left < right ): ##因为left == right的时候，在[left, right)是无效的空间
            middle = int(left + ((right - left)/2)) ## 防止溢出，等同於(left + right) / 2
            if (nums[middle] > target):
                right = middle ## target 在左区间，在[left, middle)中
            elif (nums[middle] < target):
                left = middle + 1 ## target 在右区间，在 [middle+1, right)中
            else: ## nums[middle] == target
                return middle 
          
        ## 分别处理如下四种情况
        ## 目标值在数组所有元素之前 [0,0)
        ## 目标值等于数组中某一个元素 return middle
        ## 目标值插入数组中的位置 [left, right) ，return right 即可
        ## 目标值在数组所有元素之后的情况 [left, right)，return right 即可

        return right