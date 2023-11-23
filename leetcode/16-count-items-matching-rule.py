def countMatches(items, ruleKey, ruleValue):
        
        number_of_items = 0
        index = 0 # assuming i = type
        if ruleKey == "color":
            index = 1
        if ruleKey == "name":
            index = 2

        for item in items:
            print(item[index])
            if ruleValue == item[index]:
                number_of_items = number_of_items + 1
        
        print(number_of_items)
        return number_of_items
    
items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]] 
ruleKey = "type"
ruleValue = "phone" 
print(countMatches(items,ruleKey,ruleValue))   



       
                  
        