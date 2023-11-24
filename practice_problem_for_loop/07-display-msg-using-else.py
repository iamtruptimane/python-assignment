# we are printing the first 5 numbers, 
# and after successful execution of a loop, 
# the interpreter will execute the else block.
#Defining the else part with for loop is optional.

def display_msg_using_else():
    
    for i in range(5):
        print(i)
    else:
        print("Done")  
display_msg_using_else()  

# else block will be skipped when:

#for loop terminate abruptly
#the break statement is used to break the loop        