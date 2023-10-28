# the value of input function is always a string
def func1():
    
    name = input("type your name :")
    age = int(input("type yoyr age :")) # typecasting
    #we have to convert strg into int to do some arthimatic operations

    print(f"{name} is {age} years old")
    print(f"trupti's sister is {age - 10} years old")

    inputstring = input("enter a string: ")
    print(inputstring, sep="#" , end="&\n")

    inputstring2 = input("enter anothr string :")
    print(inputstring, inputstring2 , sep="#", end="&")
#func1()    

def func2():
    print(int(15.5)-10)
    print(float(15.5)-10)
    
func2()    


