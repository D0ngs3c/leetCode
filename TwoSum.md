'''
class Solution():
    def __init__(self, nums, target):
        
        self.nums = []
        self.target = target
        
    def twoSum(self, nums, target):
                             
        for i in range(0,len(nums)-1): 
            j = len(nums) - 1
           
            while i < j :
                sum = nums[i] + nums[j]
                if sum == target :
                    print('[%d,%d]'%(i,j))
                j -= 1		
'''
