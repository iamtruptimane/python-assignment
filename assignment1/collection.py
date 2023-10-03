def func():
    list_1 = [10,20,30,40,50,57,70,80,90,100]
    print(list_1)
    print(f"type of list = {type(list_1)}")
    print(f"total elements in list = {len(list_1)}")
    
    index_position= list(range(0,10))
    print(index_position)
    
    # for i in range(len(list_1)):
    #     print(f"value at {i} is {list_1[i]}")
        
    i = len(list_1) - 1 #reversing array
    while(i >= 0):
        # logic
        print(f"value at {i} is {list_1[i]}")
        if list_1[i] % 2 == 0:
            print(f"{list_1[i]} is even ")
        else:
            print(f"{list_1[i]} is odd ")
                
        # increament/ decreament
        i = i - 1
        
    
    
    # for i in index_position:
    #     print(f"value at {i} is {list_1[i]}")
        
func()        
    
    
