from math import factorial as f


nPr = lambda n, r: f(n) / f(n-r)
nCr = lambda n, r: f(n) / f(r) / f(n-r)
round6 = lambda n: str(n) + '0' * 5 if n.is_integer() else str(round(n, 6))
compare = lambda lst: sum(1 for i, n in enumerate(lst) if i + 1 != n)


def expected(lst):
    res = 0.0
    for i in range(1, compare(lst)):
        res += nCr(10, i + 1)
    return round6(res)


def main():
    output = []
    t = int(input())
    
    for _ in range(t):
        l = map(int, input().split())
        output.append(expected(l))
        
    for out in output:
        print(out)


if __name__ == '__main__':
    main()