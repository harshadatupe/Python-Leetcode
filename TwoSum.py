class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        length = len(nums)
        while(i<length):
            key = target - nums[i]
            j=i+1
            while(j<length):
                if(key==nums[j]):
                    return (i,j)
                j=j+1
            i=i+1
        return i,j 
            

