import time 
start = time.perf_counter_ns()
def prime_factors(n):
    i = 2
    prime_factors_list = []
    while n != 1:
        if n % i:
            i+= 1
        else:
            n = n // i
            prime_factors_list.append(i) 
    return prime_factors_list

print(prime_factors(12))
end = time.perf_counter_ns()
print(end-start)