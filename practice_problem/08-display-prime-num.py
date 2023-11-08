def display_prime_num():
    
    for num in range(25,51):
         # all prime numbers are greater than 1
         # if number is less than or equal to 1, it is not prime
        
        if (num > 1):
            for i in range(2,num):
                if(num % i) == 0:
                    # not a prime number so break inner loop and
                    # look for next number
                    break
            else:
                print(num)
display_prime_num()                    
            
        