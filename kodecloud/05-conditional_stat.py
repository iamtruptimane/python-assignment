def func1():
    age = int(input("what's your age? "))

    if age >= 18:
        print("you are an adult!")
    else:
        print("you are not an adult")    
#func1() 

def func2():
    x = 3
    if (x == 0):
        print("i am here!")
    elif (x == 3):
        print("or here!")
    print("or over here!") 
#func2()

def func3():
    x = 0
    a = 6
    b = 6
    
    if a > 0:
        if b < 0:
            x = x + 6
        elif a > b:
            x = x + 5
        else:
            x = x + 4
    else:
        x = x + 7
    print(f"value of x = {x}")    
#func3()

def func4():
    
    if True: print("hello")
    
    #if (5,10):
    #print("hello")
    
    #if (yes):
        #print("hello")
        
    if(5,10): print("hello")  
func4()          
                                      
            
           