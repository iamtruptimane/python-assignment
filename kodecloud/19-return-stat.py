# func always don't have to ruturn any value 

def print_sum(num1,num2):
    sum = num1 + num2
    print("The sum is:", sum)
#print_sum(10,20)

#but if you want to use sum variable outside the function then you have to return the arguments

def print_sum(num1,num2):
    return num1 + num2
#sum = print_sum(10,20)
#print("The sum is:",sum) 

# after return statment func stops it's execution
def print_sum(num1,num2):
    sum = num1 + num2
    if(sum == 0):
        return
    print("The sum is:",sum)
#print_sum(4,2) 
#print_sum(-1,1) 

# python always return some value which is none = variable doesn't have any value
def is_even(num):
    if(num % 2 == 0):
        return True
#print(is_even(6))
#print(is_even(7)) 

def My_function(x):
    return 10 - x
#print(My_function(4))

def return_greeting():
    return "Hello World"
#print(return_greeting()) 

def is_true(a):
    return bool(a)

#result = is_true(6<3)
#print("The result is", result)   

def square(i):
    j = i * i
    return j 
#print(square(3))

def square(i):
    j = i * i
    return j
num = 2
result = square(num) 
print("The result of", num , "is", result)  
         
     