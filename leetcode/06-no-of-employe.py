def numberOfEmployeesWhoMetTarget(hours,target):
        count = 0
        for hour in hours:
            if hour == target or hour > target:
                count = count + 1

                
        return count
    
hours = [5,1,4,2,2]
target = 6
print(numberOfEmployeesWhoMetTarget(hours,target))    