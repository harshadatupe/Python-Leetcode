# finding a pair in an array who's addition is a given number

# basic approach: Time Complexity: O(n^2), Space Complexity: O(n)
nums = [1,2,3,4,5]
target = 6
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
            

