def func1():
    age_1 = int(input("type your age: "))
    age_2 = int(input("type your age: "))
    
    if (age_1 >=18 and age_2 >= 18):
        print("You both are adult")
    elif (age_1 >= 18 or age_2 >= 18):
        print("one of you is an adult")
    else:
        print("you both are childrens")
#func1()

def func2():
    is_hungry = True
    
    
    if(not is_hungry):
        print("You are not hungry")
    else:
        print("You are hungry")    
#func2()

def func3():
    x = 6
    print(x > 7 or x < 12) # it will return boolean value
#func3()

def func4():
    x = 6
    y = 7
    print(x == y)
func4()        
         
               
    