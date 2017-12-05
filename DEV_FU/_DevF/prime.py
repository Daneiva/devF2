def is_prime(n):
    div = 2
    if n == 1:
        return False
    while (div < n / 2):
        if (n % div == 0):
            return False
            div += 1
    return True


#if __name__ == "__main__":

# print("5 is prime:", is_prime(5))
# print(is_prime(4))
# print(is_prime(1))
# print(is_prime(54654654654654654654888999))
