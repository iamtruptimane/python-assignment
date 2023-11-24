def kidsWithCandies(candies, extraCandies):

        result = []
        greatest = 0
        

        for candy in candies:
            if greatest < candy:
                greatest = candy
        
        for candy in candies:
            sum = candy + extraCandies            
            if sum >= greatest:
                result.append(True)
            else:
                result.append(False)
        return result 
     
candies = [4,2,1,1,2]
extraCandies = 1

print(kidsWithCandies(candies, extraCandies))
                      