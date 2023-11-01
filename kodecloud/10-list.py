def func1():
    contries = ["USA", "canada", "India"]
    print(contries)
    print(len(contries)) # returns no of element in list
    print(contries[0])
    print(contries[1])
    print(contries[2])
    
    contries[0]= "uk" # change value at specific index
    #contries[3]= "Africa" error : list assignment index out of range
    print(contries)
    print(len(contries))
    print(contries[0])
    print(contries[1])
    print(contries[2])
    
    del contries[1] # to delete element at specific index
    print(contries)
    
    print(contries[-1]) # to get last element in list
    print(contries[-2]) # to get 2nd last element in list
#func1()

def reverse_list():
    list_1 = [2,3,5,7,8]
    print(list_1) # print(list_1[0:5:1]) or list_1[::] or list_1[0:] or list_1[:5]
     
    print(list_1[::-1])
    
#reverse_list()

def func2():
    list_1 = [2,3,5,7,8]
    print(list_1)
    
    print(list_1[0:5:2]) # print elements at even index # start at 0 index
    print(list_1[1:5:2])# print elements at odd index # start at 1 index
    print(list_1[::3])# print elements by skipping 2 index # start at 0 index
#func2()    
        
    
        
    