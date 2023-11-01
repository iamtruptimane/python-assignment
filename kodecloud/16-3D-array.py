def func1():
    school = [
        [
            ["r","s","v"],
            ["p","w","q"],
            ["s","f","a"],
        ],
        [
            ["w","r","t"],
            ["s","f","h"],
            ["r","l","j"],
        ],
        [
            ["e","r","d"],
            ["f","s","w"],
            ["a","e","f"],
        ]
        
    ]
    letter = school[2][1][1]
    print(letter)
#func1()

def func2():
    matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
    print(matrix[1][1][1])
#func2()

def func3():
    matrix = [[[0,1,2],[0,1,2],[0,1,2]],[[0,1,2],[0,1,2],[0,1,2]],[[0,1,2],[0,1,2],[0,1,2]]] 
    matrix2=[]
    
    for submatrix in matrix:
        for val in submatrix:
            for i in val:
                matrix2.append(i)
    print(matrix2)
#func3()
def func4():
    Colors= [
             [['Blue','Green','White','Black']], 
             [['Green','Blue','White','Yellow']], 
             [['White','Blue','Red','Green']] 
            ]
    print(Colors[2][0][2])
func4()    
                   
           
           
       
        
    