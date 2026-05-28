class ModOfTwo:

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):

        if self.n <= self.max:

            result = self.n % 2
            self.n += 1

            return result

        else:
            raise StopIteration


mod = ModOfTwo(3)

iterator=iter(mod)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
