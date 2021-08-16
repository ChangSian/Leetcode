## two pointer (Time Limit Exceeded)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        start = 0
        end = 1
        maxarea = 0
        len_h = len(height)
        

        while start < end and end < len_h:

            newarea = (end-start) * min([height[start], height[end]])
            end += 1

            if newarea > maxarea:
                maxarea = newarea

            if end >= len_h:
                start += 1
                end = start + 1
                
        return maxarea

## two pointer (Time Limit Exceeded)
##Runtime: 708 ms, faster than 80.04% of Python3 online submissions for Container With Most Water.
##Memory Usage: 27.5 MB, less than 57.05% of Python3 online submissions for Container With Most Water.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        start = 0
        end = len(height)-1
        maxarea = 0
        

        while start < end :
            
            newarea = (end-start) * min([height[start], height[end]])

            if newarea > maxarea:
                maxarea = newarea

            if height[start] <= height[end]:
                start += 1
            else:
                end -=1
                
        return maxarea