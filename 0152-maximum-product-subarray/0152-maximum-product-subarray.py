class Solution(object):
    def maxProduct(self, nums):
        curr_max=nums[0]
        curr_min=nums[0]
        max_prod=nums[0]
        for i in range(1,len(nums)):
            temp_min=curr_min
            temp_max=curr_max
            curr_max=max(nums[i],curr_max*nums[i],temp_min*nums[i])
            curr_min=min(nums[i],curr_min*nums[i],temp_max*nums[i])
            max_prod=max(max_prod,curr_max,curr_min)
        return max_prod
            
        