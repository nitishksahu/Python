class Car():

    model= 2016

    def __init__(self, name):
        name = name
        print(name, ' car Created of model', self.model)


class PrivateCar(Car):

    def drive(self):
        print('Car is driving.....')

car1 = PrivateCar('Volvo')
car1.drive()
car2 = PrivateCar('Audi')
car2.drive()

