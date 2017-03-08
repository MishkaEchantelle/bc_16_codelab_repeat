
class Car(object):

    def __init__(self, name='General', model='GM', car_type='saloon'):

        self.name = name
        self.model = model
        self.car_type = car_type
        
        
        self.speed = 0
        self.num_of_doors = self.get_num_of_doors()
        self.num_of_wheels = self.get_num_of_wheels()

    def is_saloon(self):

        return self.car_type == 'saloon'

    def get_num_of_doors(self):

        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            return 2
        else:
            return 4

    def get_num_of_wheels(self):

        if self.car_type == 'trailer':
            return 8
        else:
            return 4

    def drive(self, num):

        if self.car_type == 'saloon':
            self.speed = 10 ** num
        else:
            self.speed = 77

        return self