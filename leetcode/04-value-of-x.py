def finalValueAfterOperations(operations):
        x = 0
        
        for operation in operations:
            if operation == "X++" or operation == "++X":
                x = x + 1
            if operation == "--X" or operation == "X--":
                x = x - 1
        return x 
    
operations = ["X++","++X","--X","X--"]
print(finalValueAfterOperations(operations))               
            


    

        