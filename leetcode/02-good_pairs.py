
def numIdenticalPairs(nums) :

        good_pairs = 0

        i = 0
        while(i < len(nums)):
            j = i + 1
            while(j < len(nums)):
                # print("nums[i] == nums[j] ", nums[i] , nums[j])
                # print("[i] <[j] ", i , j)

                if nums[i] == nums[j] and i < j:
                    good_pairs = good_pairs + 1

                j = j + 1
            i = i + 1

        return good_pairs
    

good_pairs = [1,2,3,1,1,3]
print(numIdenticalPairs(good_pairs))



        
        