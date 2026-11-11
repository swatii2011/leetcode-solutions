class Solution(object):
    def majorityElement(self, nums):
        candidate1=None
        candidate2=None
        count1=0
        count2=0
        for i in nums:
            if i==candidate1:
                count1+=1
            elif i==candidate2:
                count2+=1
            elif count1==0:
                candidate1=i
                count1=1
            elif count2==0:
                candidate2=i
                count2=1
            else:
                count1-=1
                count2-=1
        count1=nums.count(candidate1)
        count2=nums.count(candidate2)
        res=[]
        if count1>(len(nums))//3:
            res.append(candidate1)
        if count2>(len(nums))//3:
            res.append(candidate2)
        return res
        