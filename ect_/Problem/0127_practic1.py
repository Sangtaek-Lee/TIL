class Doggy:

    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, birth):
        self.name = name
        self.birth = birth
        self.plus()

    @classmethod
    def plus(cls):
        cls.num_of_dogs += 1
        cls.birth_of_dogs += 1

    @classmethod
    def get_status(cls):
        print(f'Birth: {cls.birth_of_dogs}, Current: {cls.num_of_dogs}')

    def bark(self):
        print('왈왈!')

    def __del__(self):
        self.num_of_dogs -= 1

d1 = Doggy('초코', '푸들')
d2 = Doggy('꽁이', '말티즈')
d3 = Doggy('별이', '시츄')

d1.bark()
d2.bark()
d3.bark()

Doggy.get_status()