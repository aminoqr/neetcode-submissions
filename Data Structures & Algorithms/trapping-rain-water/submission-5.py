class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        l_arr = [0] * n
        r_arr = [0] * n
        
        max_height = 0
        for i in range(n):
            l_arr[i] = max_height
            max_height = max(max_height, height[i])
            
        max_height = 0
        for i in range(n-1,-1,-1):
            r_arr[i] = max_height
            max_height = max(max_height, height[i])

        for i in range(len(height)):
            water = min(l_arr[i], r_arr[i]) - height[i]
            if water > 0:
                ans += water 

        return ans


       
