def square(num):
    return num ** 2

MYfunc=square #aliase
print(f"square of 5={square(5)}")
print(f"square of 10={MYfunc(10)}") #aliase

def cube(num):
    return num ** 3
    
MYfunc1=cube
print(f"cube of 3={cube(3)}")
print(f"cube of 2={MYfunc1(2)}")    
    