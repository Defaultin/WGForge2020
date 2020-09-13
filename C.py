def tanks_game(n, m, k):
    '''
    If from position x you can get into a losing one, then position x is a winning one
    If all moves from position x lead to winning positions, then position x is losing
    Winning strategy: putting the opponent in a losing position
    '''
    if k < n and k < m:
        t = [['-'] * n for i in range(m)]
        for i in range(n):
            t[0][i] = '+' if i % 2 else '-'
        for i in range(m):
            t[i][0] = '+' if i % 2 else '-'

        for l in range(1, max(n, m)):
            for i in range(l, n):
                try:
                    if t[l-1][i] == '-' or t[l][i-1] == '-' or (l >= k and i >= k and t[l-k][i-k] == '-'):
                        t[l][i] = '+'
                except IndexError:
                    pass

            for i in range(l, m):
                try:
                    if t[i][l-1] == '-' or t[i-1][l] == '-' or (i >= k and l >= k and t[i-k][l-k] == '-'):
                        t[i][l] = '+'
                except IndexError:
                    pass

        return t[-1][-1]
    else:
        return '+' if (n + m) % 2 == 1 else '-'


def main():
    output = []
    t, k = map(int, input().split())
    for _ in range(t):
        n, m = map(int, input().split())
        output.append(tanks_game(n, m, k))

    for out in output:
        print(out)


if __name__ == '__main__':
    main()