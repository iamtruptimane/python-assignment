def maximumWealth(accounts):
        
        max_wealth = 0
    

        for account in accounts:
            wealth = 0
            for num in account:
                wealth = wealth + num
            
            if (max_wealth < wealth):
                max_wealth = wealth

        return max_wealth

accounts = [[1,5],[7,3],[3,5]]
print("Richest customer wealth = ", maximumWealth(accounts))    