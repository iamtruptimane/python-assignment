def print_pattern():
    
    row = 5
    
    for i in range(1, row + 1):
        for j in range(1, i + 1 ):
            print(j, end = " " )
        print("") 
           
print_pattern() 

def print_pattern_reverse():
    n = 5
    k = 5
    for i in range(0,n + 1):
        for j in range(k - i, 0, -1):
            print(j, end = " ")
        print("")    
print_pattern_reverse()

def print_design():
    row = 5
    
    for i in range(0,row):
        for j in range(0,i + 1):
            print("*", end= " ")
        print("\r")
    for i in range(row, 0, -1):
        for j in  range(0, i - 1):
            print("*", end = " ")
        print("\r")
        
print_design()

def print_table_chart():
    
    for i in range(1, 11):
    # nested loop
    # to iterate from 1 to 10
        for j in range(1, 11):
        # print multiplication
            print(i * j, end=' ')
        print()  
print_table_chart()                          
                       