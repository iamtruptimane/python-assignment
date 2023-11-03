# variables which are declared inside the function body cannot be accessible outside the func
def input_number():
    result = int(input("Enter a num: ")) * 100 
    return result # local scope variable
#print(result) error : NameError: name 'result' is not defined

num = 100 # global scope variable
def input_num():
    num = 50 # local scope variable
    result= int(input("Enter a num: ")) * num
    return result
#print(num) # it will print global scope variable
#print(input_num())

#x = 30
def my_func():
    x = 20
    print(x , end=" ")
    
#my_func()
#print(x, end=" ") 

#x = 30
def My_func():
    global x
    x = 20
    
#print(My_func())
#print(x) 

#x = 20
def My_func():
    print(x, end = " ")
    
#My_func()
#print(x, end =" ")  

def My_func():
    def My_inner_func():
        x = 20
    print(x)
    My_inner_func()
#My_func() error : name "x" is not defined

def My_func():
    x = 20
    def My_inner_func():
        print(x)
    My_inner_func()
My_func()                                     

