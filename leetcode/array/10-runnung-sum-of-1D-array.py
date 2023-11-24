def runningSum(nums):
        
        sum = 0
        arr = []


        for num in nums:
            sum = sum + num
            arr.append(sum)
        
        return arr
    
nums = [1,1,1,1,1]
print(runningSum(nums))    
        
