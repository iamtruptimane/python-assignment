def cube_of_num():
    x = int(input("Enter a Number: "))
    
    for num in range(1,x+1):
        cube = num ** 3
        print(f"Current Number is : {num} and the cube is {cube}")
cube_of_num()        
         