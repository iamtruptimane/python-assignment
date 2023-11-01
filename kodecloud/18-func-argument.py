def input_number(num):
    return int(input("Enter a number: ")) * num
#input1 = input_number(10)
#print(input1)

def input_number(num1,num2):
    return int(input("Enter a number: ")) * num1 - num2
#input1 = input_number(10,2)
#print(input1)

def input_number(num=10):
    return int(input("Enter a number: ")) * num
#print(input_number())

def fullname_func(fname):
    print(fname + " Mark")
#fullname_func("john")

def add_num(num):
    return int(input()) + num
#print(add_num(5))

a=0
def add_three(a):
    return a + 3 
#result = add_three(a)
#print(result)

def My_func(*friends):
    print("The tallest student is " + friends[0])
#My_func("ros","sam", "era")  

a=0
def add_three(a):
    return a + 3
#result = add_three(6) 
#print(result)

def fullname_func(fname, lname):
    print(fname + " " + lname)
#fullname_func("John", "Mark")

nums=[7,4,1]
def change_third_item(list):
    list[2] = 5
change_third_item(nums) # nums=list (aliase)
print(nums)        
    