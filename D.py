from functools import lru_cache


def round6(n):
	'''45.0 -> 45.000000'''
	n = str(round(n, 6))
	return n + '0' * (6 - len(n.split('.')[-1][:6]))


def get_expected(lst):
	'''Math expected value'''
	total, permutation = 45, 0
	lenght = len(lst)

	for i in range(lenght - 1):
		for j in range(i + 1, lenght):
			if lst[i] > lst[j]:
				lst[i], lst[j] = lst[j], lst[i]
				total += reduce(tuple(lst), lenght)
				permutation += 1
				lst[i], lst[j] = lst[j], lst[i]

	return total / permutation


@lru_cache(maxsize=4037904)
def reduce(lst, lenght=10):
	'''Reduces the permutation list'''
	left, right = 0, 0

	for i in range(lenght):
		if lst[i] != i:
			left = i
			break

	for i in range(lenght - 1, left, -1):
		if lst[i] != i:
			right = i
			break

	size = right - left + 1
	if size == lenght:
		return get_expected(list(lst))
	elif 1 < size < 10:
		return get_expected([lst[left + i] - left for i in range(size)])
	else:
		return 0.0


def main():
	output = []
	t = int(input())
	
	for _ in range(t):
		l = tuple(map(lambda x: int(x) - 1, input().split()))
		output.append(reduce(l))
		
	for out in output:
		print(round6(out))


if __name__ == '__main__':
	main()