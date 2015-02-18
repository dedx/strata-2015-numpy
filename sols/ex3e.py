def eratosthenes_sieve(maximum):
    """Use the famous sieve of Eratosthenes to find all the
       prime numbers between 2 and maximum.
            Input: maximum range for the primes
            Output: NumPy array of prime numbers between 2 and maximum
    """
    numbers = np.ones((maximum,), dtype=bool)
    numbers[0]=False
    numbers[1]=False
    for i in range(2,maximum):
        numbers[2*i::i]=False
    return np.nonzero(numbers)
