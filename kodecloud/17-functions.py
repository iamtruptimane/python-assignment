def multi_num(num):
    return int(input()) * num

#print(multi_num(5))

def multi_func():
    result = int(input()) * 5
    return result
#print(result) error :result is not global variable

a=0
def add_one(a):
    return a +1
result=add_one(a)
#print(result) # result get printed coz this variable declared outside func 

def print_info(name, age=18):
    print(name,age)
#print_info("john",19) 

def multi_func(num1,num2):
    return num1 * num2
#print(multi_func(5,num1=10)) 
#error: multi_func() got multiple values for argument 'num1'
#print(multi_func(5,10)) 

def My_func(*students):
    print("The tallest student is " + students[2]) 
My_func("james","Ella","jackson")

    