numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes  = []
numbers.remove(1)
for i in numbers:
    #count = 0
    is_primes = True
    for j in range(2, i):
        if i % j == 0 and i != j:
            #count += 1
            is_primes = False
    #if count == 0:
    if is_primes:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)


