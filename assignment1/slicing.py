def func1():
    
    list_1 = [10,20,30,20,40,30,50,60,50,70,30]
    print(list_1)
    
    position= range(len(list_1)) #position = [0,1,2,3,4,5,6,7,8,9,10]
    
    for i in position:
        x= list_1.count(30)
        
    print(f" 30 repeated {x} times")
#func1() 

def func2():
    
    list_2 = [10,20,30,40,50,60,70,80,90,100] 
    print(list_2)
    numbers = []
    
    slice = range(2,7) # slice = [2,3,4,5,6] 
    
    for i in slice:
        numbers.append(list_2[i]) 
    
    print(numbers) 
    
#func2()

def func3():
    
    list_3 = [2,3,4,5,6,7,8,9]  
    print(list_3)
    even_num = [] # give me all even numbers
    
    position = range(len(list_3)) #position = [0,1,2,3,4,5,6,7]
    
    for i in position: 
        if list_3[i] % 2 == 0:
            even_num.append(list_3[i])
            
    print(f"even_num = {even_num}")
    
#func3() 

def func4():
    list_4 = [1,3,2,5,4,5,7,8]  
    print(list_4)
    even_index_num = [] # give me all the values which are present at even index postion
    
    postion = range(len(list_4)) # position = [0,1,2,3,4,5,6,7]
    
    for i in postion:
        if i % 2 == 0:
            even_index_num.append(list_4[i])
            
    print(f"even_index_num = {even_index_num}")
    
func4()            
    
                
    
          
        

       