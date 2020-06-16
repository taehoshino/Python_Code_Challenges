import math


def get_prime_factor(number):
    sqrt_number = math.ceil(math.sqrt(number))
    prime_list = []
    i = 2
    while i <= sqrt_number:
        if number % i == 0:
            prime_list.append(i)
            number = number / i
        else:
            i += 1

    if number != 1:
        prime_list.append(number)

    return prime_list


print(get_prime_factor(13))

