def factorial_of_num():
    
    num = 5
    fact = 1
    
    if (num < 0):
        print("factorial does not exist for negative numbers")
        
    elif(num == 0):
        print("factorial of zero is one")
            
    else:        
            # run loop 5 times
        for i in range(1, num + 1):
            fact = fact * i
        print(fact)
        
factorial_of_num()        