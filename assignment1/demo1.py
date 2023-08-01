def func1():
    num=[10,20,30,40,50,60]
    print(num)
    for n in num:
        print(n)
        
    print(f"total value in num={len(num)}") 
    print(f"range of num= {range(len(num))}")   
    print(list(range(2,6))) 
    print(range(2,6))   
    print(f"num at 0th= {num[0]}")
    print(f"num at 1th= {num[1]}")
    print(f"num at 2th= {num[2]}")
    print(f"num at 3th= {num[3]}")
    print(f"num at 4th= {num[4]}")
    print(f"num at 5th= {num[5]}")
    
    #index_pos=[0,1,2,3,4,5]
    index_pos=range(len(num))
    for i in index_pos:
        print(f"num at {i} pos = {num[i]}")
    index_pos1=list(range(2,6))
    for i in index_pos1:
        print(f"value at {i} = {num[i]}")
        
#func1()

def func2():
    colours=["red","black", "yellow", "green", "orange"]
    print(colours)
    for colour in colours:
        print(f"colourr={colour}")
        
    print(range(len(colours)))
    
    index_pos=range(len(colours)) #index_pos=[0,1,2,3,4]
    for i in index_pos:
        print(f"colour at {i} = {colours[i]}")
        
    index_pos=list(range(1,3)) #index_pos=[1,2]
    for i in index_pos:
        print(f"value at {i}= {colours[i]}")
func2()                        
     
        