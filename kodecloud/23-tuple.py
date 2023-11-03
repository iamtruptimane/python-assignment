# tuple is immutable data type which cannot be modyfied

def func1():
    tuple = (1,2,3)
    print(tuple)
    tuple2 = 1,2,3
    print(tuple2)
#func1()

def func2():
    tuple1 = (1,2,3)
    for item in tuple1:
        print(item)
#func2()

def func3():
    tuple1 = (1,2,3,4)
    print(tuple1[0:2]) 
#func3()

# we cannot modify tuple
def func4():
    tuple1 = (1,2,3)
    tuple1.append(4)
    tuple1[1]=9
    del tuple1[1]
#func4() error : 'tuple' object has no attribute 'append'

def func5():
    tuple1 = (1,) # if one element in tuple then give "," to differntiate bet regular var and tuple
    tuple2 = 1,
    print(tuple1)
    print(tuple2)
#func5() 

#x = tuple(3)
#print(x) #error : 'int' object is not iterable

def func6():
    a = (10, [20,30], 40, 50)
    print(a[1][1], end = " ")
    print(a[0], end = " ")
    print(a[1][0], end = " ")
#func6()

def func7():
    a = (10,20,30,40,50)
    a = a[::-1]
    print(a)
func7()    
        

   
     

   
                   