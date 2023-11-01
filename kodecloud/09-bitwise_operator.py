def func1():
    print(15 | 22) # one of them is 1 returns 1 or both of them is 1 returns 1 , both of them 0 returns 0
    print(15 & 22) # only both of them is 1 return 1 ,if either one of them is 0 or both of 0 returns 0
    print(15 ^ 22) # only one of them is 1 returns 1 if either is 1 or either is 0 returns 0
    print( 5 ^ 11)
    print(~22) # it will returns 1 for every 0 and returns 0 for every 1
    print(~200)
#func1()

def bit_shifting():
    print(22 >> 1) # right shifting
    print(22 >> 2)
    print(22 << 1) # left shifting 
    print(22 << 2) 
    
    # right shifting =
    # print(22 //2) == print(22 >> 1) = 11
    # print(22 // 4) == print(22 >> 2) = 5
    
    # left shifting
    # print(22 * 2) == print(22 << 1) = 44
    # print(22 * 4) == print(22 << 2) = 88
    # print(22 * 8) == print(22 << 3) = 176
#bit_shifting()

def func2():
    a = 20
    b = 5
    print("a | b", a | b)
    print(int(1001))
func2()

        
      