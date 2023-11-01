#slicing
#list[start:end]
def slicing_list():
    letters = ["A", "B", "C", "D"]
    print(letters)
    
    First_Two_letters = letters[0:2]
    print(First_Two_letters)
    
    # in all following cases we are creating a new list without disturbing original list
    print(letters[1:])
    print(letters[:3])
    print(letters[1:-1])
    
    # in this case er are modifying original list
    del letters[:] # it will return empty list
    print(letters)
#slicing_list() 

#def func1(): error: list object has no attribute upper
    #list1 = [1, 66, "python", [11, 55, "cat"], [ ], 2.22, True]
    #print(list1.upper())  
#func1() 

def func2():
    list_1 = [0,3,4,1,2]
    print(list_1)
    list_1[2:4]=[1,2]
    print(list_1) 
#func2()  

def func3():
    list_1 = [0,3,4,1,2]
    print(list_1)
    
    list_1[2:5]=[8,9]
    print(list_1)
func3()         
    
    
    
    
    