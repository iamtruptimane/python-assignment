# Write a program to calculate the sum of series up to n term.
# For example, 
# if n =5 the series will become 
# 2 + 22 + 222 + 2222 + 22222 = 24690
def sum_of_series():
    n = 5
    start = 2
    sum_seq = 0
    
    for num in range(0,n):
        print(start, end = " + ")
        
        #modify sum_seq
        sum_seq = sum_seq + start
        
        #modify start
        start = start * 10 + 2
    print("\nSum of above series is: ", sum_seq)    
sum_of_series()  

