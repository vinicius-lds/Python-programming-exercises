class Person(object):
    name = 'Person'

    def __init__(self, name, *args, **kwargs):
        self.name = name
        return super().__init__(*args, **kwargs)

p = Person('Vinícius')
print(p.name)
print(Person.name)
