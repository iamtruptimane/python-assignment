def leftRightDifference(nums):    
        leftsum = []
        rightsum = []
        answer = []
        sum = 0

        i = 0
        while(i < len(nums)):
            if i == 0:
                leftsum.append(0)
            else:
                sum = sum + nums[i-1]
                leftsum.append(sum)
            i = i + 1 
        j = len(nums)-1
        sum = 0
        while(j > -1):
            if j == (len(nums)-1):
                rightsum.append(0)
            else:
                sum = sum + nums[j + 1]
                rightsum.append(sum)
            j = j - 1   
        rightsum.reverse()
        i=0
        while(i < len(leftsum)):
            sub = leftsum[i] - rightsum[i]           
            if sub < 0:
                sub = sub * -1
            answer.append(sub)
            i = i + 1    
        return answer  
nums = [10,4,8,3]
print(leftRightDifference(nums))
                      
