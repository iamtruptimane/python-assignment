age = 22
def multiply(num):
    num = num * 2
    print(num)
#multiply(age) # age = num = 22 * 2 = 44
#print(age) # age = 22 global variable # original unchanged

# variable that have list values stored with a pointer to the location of list in memory
nums = [1,2,3]
def change_first_item(list):
    list[0] = 9
#change_first_item(nums) # nums = list = [9,2,3]
#print(nums) # nums = [9,2,3] # original also changed 

def My_function(*argv):
    print(argv)
#My_function('Hello', 'World!')# print it as a tuple

def My_func(*argv):
    print(argv[2])
#My_func("Hello", "World") error: tuple index out of range 

def my_func(arg1, *argv):
    print("First argument:", arg1)
    for i in argv:
        print("Next argument: ", i)
#my_func("welcome", "to", "python!") 

def sum(*args):
    result = 0
    for i in args:
        result = result + i
        return result
#print(sum(2,3,1))

def division(a,b):
    return a/b
division(8,2)            
        
       