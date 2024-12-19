class Solution(object):
    def sortColors(self, nums):
        a=[0,0,0]
        for i in nums:
            a[i]+=1
        del nums[:]
        for i in range (3):
            for j in range (a[i]):
                nums.append(i)
        print(nums)
        return nums