import time
start = time.perf_counter_ns()
def factors(value:int)->list[int]:
    prime_list_factors = []
    
    def is_prime_number(n):
        first_form = (n-1) / 6
        second_form = (n+1) / 6
        if first_form.is_integer() or second_form.is_integer():
            return True
        elif n in [2, 3]:
            return True

    if value < 5:
        limit_search = value
    else:
        limit_search = int((value)** (1/2))
    for n_search in range(2,  limit_search + 1):
        if value % n_search == 0 and is_prime_number(n_search):
            value//= n_search
            prime_list_factors.append(n_search)
            return prime_list_factors + factors(value)
        elif n_search == limit_search:
            prime_list_factors.append(value)

    return prime_list_factors

print(factors(12))
end= time.perf_counter_ns()
print(end - start)