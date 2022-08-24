def sum_digits(n):
    
    assert n >= 0 #assert just means "while this condition remains 
        #true, run the code assuming this condition stays true"
    
    if n < 10: # Base case, only happens when there's 1 remaining digit
        return n
    
    return sum_digits(n // 10) + (n % 10) # Adds the rest of the number with the final number
    
    #n % 10 has the value of n that is saved before the value of n that is returned in the line above
    #for ex: 1400 >> 140 >> 14 >> 1 (since 1 is returned the value of 14 is stoed for n % 10)
    # sum_digits(n // 10) just calls the sum_digits function again but with a simpler case in this case.


print(sum_digits(1400)) # sample test case

    
  