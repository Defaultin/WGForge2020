class Tactical_number:
    def __init__(self, max_value, weights):
        self.weights = weights
        self.max_value = max_value
        self.min_value = min(weights)
        self.min_idx = 9 - weights[::-1].index(self.min_value)
        self.max_digits = self.max_value // self.min_value
        self.target = self.max_digits * str(self.min_idx)
        self.rest = self.max_value - self.max_digits * self.min_value

    def find_maximum(self):
        for i in range(8, self.min_idx - 1, -1):
            difference = self.weights[i] - self.min_value
            if self.rest >= difference:
                replace = self.rest // difference
                self.rest -= replace * difference
                self.max_digits -= replace
                self.target = self.target[replace:] + replace * str(i + 1)

        return self.target[self.max_digits:] + self.target[:self.max_digits]

    def __repr__(self):
        return '-1' if self.max_value < self.min_value else self.find_maximum()


if __name__ == '__main__':
    max_gold = int(input())
    costs = [int(i) for i in input().split()]
    print(Tactical_number(max_gold, costs))