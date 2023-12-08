def func1():
    classroom = [
        ["sara", "jon", "kil"],
        ["mom", "boy", "ros"],
        ["don","fog", "yol"]
    ]
    student = classroom[1][2]
    print(student)
func1()

def func2():
    matrix = [[0,1,2], [0,1,2],[0,1,2]]
    matrix2=[]
    
    for submatrix in matrix:
        for val in submatrix:
            matrix2.append(val)
    print(matrix2)
func2() 

def func3():
    matrix = [[j for j in range(3)] for i in range(3)]   
    print(matrix[1][2])
func3()

def func4():
    countries = [["Egypt", "USA", "India"],["Dubai", "America", "Spain"],["London", "England","France"]]
    countries2 =[country for sublist in countries for country in sublist if len(country) < 4]
    print(countries2)
func4()

def func5():
    a = []
    for i in range(5):
        a.append([])
        for j in range(5):
            a[i].append(j)
    print(a[3][3])
func5()    
            
    
              