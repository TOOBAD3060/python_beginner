class Software:
    needs = ['system','internet']




class Developer(Software):
    def __init__(self, name):
        self.name = name
    def talk(self):
        print('I love coding')

toobad = Developer('Olalere')

print(toobad.needs,toobad.name)
toobad.talk() 