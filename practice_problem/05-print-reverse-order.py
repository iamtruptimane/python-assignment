def reverse_order1():
    list1 =  [10, 20, 30, 40, 50]
    
    for i in list1[::-1]:
        print(i)
#reverse_order() 

def reverse_order2():
    list1 =  [10, 20, 30, 40, 50]
    
    list1 = reversed(list1)
    
    for i in list1:
        print(i)
#reverse_order2()

def reverse_order3():
    list1 =  [10, 20, 30, 40, 50]
    
    size = len(list1) - 1
    #print(size) size = [4,3,2,1,0]
    
    for i in range(size,-1,-1):
        print(list1[i])
reverse_order3()    
    


        
        