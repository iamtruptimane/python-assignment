#using lambda function
cube = lambda number : number ** 3
print(f"square of 3 = {cube(3)}")
print(f"cube={cube}")
print(f"type of cube= {type(cube)}")

lambda_add = lambda p1,p2 : p1 + p2
print(f"addition = {lambda_add(20,30)}")

def add(p1,p2):
    return p1 + p2

print(f"addition = {add(20,30)}")

lambda_mul = lambda p1,p2 : p1 * p2
print(f"multiplication = {lambda_mul(20,30)}")

def mul(p1,p2):
    return p1 * p2

print(f"multiplication = {mul(20,30)}")