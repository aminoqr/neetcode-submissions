class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftsum = [1] * n
        rightsum = [1] * n
        ans = [1] * n

        cur = 1
        for i in range(1, n):
            cur *= nums[i-1]
            leftsum[i] = cur
        cur = 1
        for i in range(n-2, -1, -1):
            cur *= nums[i+1]
            rightsum[i] = cur

        for i in range(n):
            ans[i] = leftsum[i] * rightsum[i]

        return ans