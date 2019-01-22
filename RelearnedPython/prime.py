def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, (x-1)):
            if x % n == 0:
                print(str(x) + " is not a prime")
                return False
        print(str(x) + " is a prime")
        return True

is_prime(37)
is_prime(20)