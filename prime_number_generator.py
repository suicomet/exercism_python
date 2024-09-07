
def prime_numbers_formula():
    n = 1
    while True:
        first_number = 6*n - 1
        second_number = 6*n + 1
        yield (first_number, second_number)
        n+=1

prime_numbers = prime_numbers_formula()
for _ in range (5):
    print(next(prime_numbers))