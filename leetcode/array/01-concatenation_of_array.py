
def getConcatenation(nums):
        
    
    res = nums.copy()

    print(res)
    position = range(len(nums))

    for i in position:
        res.append(nums[i])
            

    print(res)
    

nums = [1,2,1]
getConcatenation(nums)


