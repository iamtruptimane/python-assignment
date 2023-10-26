def func1():
    list_1= [10,20,30,40,50,60,70,80,90,100]
    
    print(f"number at 1st postion= {list_1[0]}")
    print(f"number at last postion= {list_1[len(list_1) - 1]}")
    print(f"number at 3rd position= {list_1[2]}")
    print(f"number at 2nd last postion= {list_1[len(list_1) - 2]}")
    
    
#func1()

def func2():
    list_2= [10,20,30,40,50,20,60,50,30,50,50,50,50]
    
    count_50= list_2.count(50)
    print(f"count 50 repeated {count_50} times")
    
    count_30= list_2.count(30)
    print(f"count 30 repeated {count_30} times")
    
#func2()

def func3():
    list_3= [10,20,30,40,50,60,70,80,90,100]
    print(list_3) 
    
    #number_reverse= list_3.copy()
    #print(number_reverse)
    #number_reverse.reverse()
    #print(number_reverse)
    list_3.reverse()
    print(list_3) 
    
#func3() 

def func4():
    
    list_4=[10,20,30,40,50,60,70,80,90,100]  
    even_index_numbers= []
    
    position= range(len(list_4))
    print(position) # range(0,10) position=[0,1,2,3,4,5,6,7,8,9]
    
    for index in position:
        if index % 2 == 0:
            even_index_numbers.append(list_4[index])
    print(even_index_numbers)
    
#func4() 

def func5():
    list_5 = [10,20,30,40,50,60,70,80,90,100]
    print(list_5)
    numbers_slice=[]
    
    position=range(2,6) # position = [2,3,4,5] range(2,6)
    print(position)
    
    for i in position:
        numbers_slice.append(list_5[i]) 
        
    print(f"number_slice={numbers_slice}") 
    
func5()                          
    