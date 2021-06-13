## 懶人Python寫法

class Solution(object):
    def removeElement(self, nums: List[int], val: int):
        i = 0
        while (i < len(nums)):
            if nums[i] == val:
                del nums[i]
                i = i-1
                i = i+1
            else: ## nums[middle] == target
                i = i+1
            
        return len(nums)
        return nums

## 暴力破解(两层for循环，一个for循环遍历数组元素 ，第二个for循环更新数组。)

class Solution(object):
    def removeElement(self, nums: List[int], val: int):
        size = len(nums)
        i = 0
        while (i < len(nums)):
            if nums[i] == val:
                for j in range(i+1, size):
                    nums[j-1] = nums[j]
                size = size - 1
                nums[size] = 101

            else:
                i = i+1

            
        return size
        return nums

## 双指针法（快慢指针法）：「通过一个快指针和慢指针在一个for循环下完成两个for循环的工作。」

class Solution(object):
    def removeElement(self, nums: List[int], val: int):
        slowindex = 0

        for fastindex in range(len(nums)):
            if nums[fastindex] != val:
                nums[slowindex] = nums[fastindex]   
                slowindex = slowindex + 1

            
        return slowindex
        return nums