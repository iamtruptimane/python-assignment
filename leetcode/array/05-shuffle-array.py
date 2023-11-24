
def shuffle(nums,n):
        i = 0
        j = n

        res = []
        
        while( i < n):
            print(nums[i], nums[j])
            res.append(nums[i])
            res.append(nums[j])

            i = i + 1
            j = j + 1

        return res

nums =  [1,2,3,4,4,3,2,1]
n = 4
print(shuffle(nums,n))     