def func1():
    for i in range(10): # range = [0,1,2,3,4,5,6,7,8,9]
        print("i is", i)
#func1() 

def func2():
    for i in range(7): # range = [0,1,2,3,4,5,6]
        if (i == 4):
            break
        print("i is", i)
#func2()

def func3():
    x = "abcd" # or x = ["a", "b", "c", "d"]
    
    for i in x:
        print(i.upper())
#func3()

def func4():
    x = "abcd"
    for i in x:
        print(i)
        x.upper()
       
#func4()

def func5():
    x = "abcd"
    
    for i in range(len(x)):
        i.upper() 
    print(x)
#func5()

def func6():
    x = "abcd"
    
    for num in range(5,11): # range = [0,1,2,3,4,5,6,7,8,9,10]
        print(num)
#func6()

def func7():
    for num in range(0,11):
        if (num % 2 == 0):
            continue
        print(num)
        
        # or if (num % 2 != 0):print(num)
#func7()

def func8(): # error : 'str' object cannot be interpreted as an integer
    x = "abcd"
    for i in range(x):
        print(i)
#func8() 

def func9(): # error : int object is not iterable
    x = 2021
    for i in x:
        print(i)
#func9()

def func10():
    x = "abcd" # try with ["abcd"]
    for i in range(len(x)): 
        print("hello")
#func10()

def func11():
    x = "abcd"
    for i in range(len(x)):
        print(i)
func11()        
                                                                          