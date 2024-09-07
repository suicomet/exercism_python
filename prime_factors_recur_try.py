def factors (value:int, prime_number_list=None)-> list[int]:
    if prime_number_list is None: 
        prime_number_list = [2, 3]
   
    def prime_numbers_formula():
        n = 1
        while True:
            first_number = 6*n - 1
            second_number = 6*n + 1
            prime_number_list.extend([first_number, second_number])
            yield prime_number_list 
            n+=1
    prime_numbers = prime_numbers_formula()
    prime_numbers_factors = []
    if value == 1:
        return prime_numbers_factors
    else:
        for prime_n in prime_number_list:
            while value % prime_n == 0:
                value //= prime_n
                prime_numbers_factors.append(prime_n)
                
    
    if value > 1:
        next(prime_numbers)
        return prime_numbers_factors + factors(value, prime_number_list)
    else:
        return prime_numbers_factors
            
      

print(factors(901255))