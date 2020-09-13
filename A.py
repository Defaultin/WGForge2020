def mult_table(size, num):
    '''How many times a number appears in the multiplication table of n*n size'''
    result = 0
    for i in range(1, size + 1):
        result += num // i <= size and not num % i
    return result


if __name__ == '__main__':
    print(mult_table(*map(int, input().split())))