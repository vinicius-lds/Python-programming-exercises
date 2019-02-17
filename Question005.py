
class Question005(object):
    def __init__(self):
        self.string = ''

    def get_string(self):
        self.string = input('Digite a string desse objeto.\n')

    def print_string(self):
        print(self.string.upper())


obj = Question005()
obj.get_string()
obj.print_string()
