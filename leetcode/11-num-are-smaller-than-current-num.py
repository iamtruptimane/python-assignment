def smallerNumbersThanCurrent(nums):

        res = []
        

        for i in nums:
            count = 0
            for j in nums:
                if j != i and j < i:
                    count = count + 1
                    
            res.append(count)
        return res
     
nums = [8,1,2,2,3]  
print(smallerNumbersThanCurrent(nums))             
        