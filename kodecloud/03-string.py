def func1():
    print("ha" * 10)
    print("ha" * 2)
    print("ha" * 0) # return empty string
    print("ha" * -1) # return empty string
#func1() 

def func2():
    cost_of_apple = 20
    amount_of_apples = int(input("how many apples do you want? "))
    
    total_sum = amount_of_apples * cost_of_apple
    print(f"you have to pay : {total_sum}")
    print(f"you have to pay :" +  str(total_sum)) 
    # typecast numeric value into string
    
#func2()

def func3():
    num = input("enter a number :")
    print(num * 3) # print("5" * 3) = 555
    
    num = int(input("enter a number:"))
    print(num * 3) # print(5 * 3) = 15
    
#func3()

def func4():
    x = 5
    y = "sally"
    
    print(str(x) +  y) 
    #print(x + y) can't concatanate str + int
func4()        

   