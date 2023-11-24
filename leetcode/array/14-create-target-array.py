def createTargetArray(nums, index):
    
        target = []

        
        i = 0 
        while(i < len(nums)):
            print(nums[i], index[i])
            target.insert(index[i], nums[i])

            i = i + 1

        return target
    
nums = [0,1,2,3,4] 
index = [0,1,2,2,1]
print(createTargetArray(nums,index))   
        