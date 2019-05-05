class Iter7(object):
    def __init__(self, n, *args, **kwargs):
        self.n = n
        return super().__init__(*args, **kwargs)

    def for_each(self):
        for n in range(self.n):
            if n % 7 == 0:
                yield n

iter7 = Iter7(150)

for x in iter7.for_each():
    print(x)
