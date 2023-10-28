def func1():
    secret_no = 3
    guess = int(input("guess no bet 0-5: "))
    
    while guess != secret_no: # stoping condition
        guess = int(input("guess no between 0-5: "))
        
    print("congratualtions you guess correct no")
#func1()

def func2():
    i = 1
    while True:
        if i % 3 == 0:
            break
        print(i) # here i = 1, i = 2
        i = i + 1
    #print(i)   here i = 3 
#func2()

def func3():
    x =1 
    while (x <= 5):
        print(x) # here x = 1, x = 2, x = 3, x = 4, x = 5
        x = x + 1 
    print(x)
#func3()

def func4():
    x = 0
    while (x < 50):
        print(x)
        x = x + 2
        
    print(x)
#func4()

def func5():
    i = 5
    while True:
        if i % 0o11 == 0:
            break
        print(i)
        i = i + 1
    print(i)    
#func5()

def func6():
    i = 1
    while True:
        if i % 0o7 == 0:
            break
        print(i)
        i = i + 1
    print(i)
#func6()

def func7():
    x = 1
    while (x < 20):
        print(x)
        x = x * 2 
    print(x)
#func7()

def func8():
    x = 2
    while(x <= 20):
        print(x)
        x = x + 2
        
#func8()

def func9():
    i = 2
    while True:
        if i % 3 == 0:
            break
        print(i)
        i = i + 2
    print(i)
#func9()

def func10():
    i = 1
    x = 3
    sum = 0
    
    while ( i <= x):
        print(f"sum={sum}")
        sum = sum + i
        print(f"i= {i}")
        i = i + 1
    print(f"last sum={sum}")    
func10()                    
        
                                   

               
                    
        
