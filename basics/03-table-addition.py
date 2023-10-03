def func(p1):
    add = 0
    i = 1
    super_add = 0
    while(i <=10):
        add= add + p1
        print(add)
        super_add = super_add + add
        
        #incerement/decrement
        i = i + 1
    print(f"super_add = {super_add}")    
        
func(2)        
    