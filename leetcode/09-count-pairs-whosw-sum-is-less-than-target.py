def countPairs(nums, target):
        
        count = 0
        i = 0
        while(i < len(nums)):
            j = i + 1
            while(j < len(nums)):
                sum = nums[i] + nums[j]
                if sum < target:
                    count = count + 1
                j = j + 1

            i = i + 1
        
        return count 
    
nums = [-6,2,5,-2,-7,-1,3]
target = -2

print(countPairs(nums, target))               
