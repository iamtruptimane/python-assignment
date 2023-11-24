# The Fibonacci Sequence is a series of numbers. 
# The next number is found by adding up the two numbers, 
# before it. 

def display_fibonacci_series():
    
    num1 = 0
    num2 = 1

    
    # if you want to run loop 10 times get range(10)
    for num in range(10):
        
        # print next number of a series
        print(num1, end = " ")
        
        # add last two numbers to get next number
        res = num1 + num2
        
        # update values
        num1 = num2
        num2 = res
display_fibonacci_series()        
        
    