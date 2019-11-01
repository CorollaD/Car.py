# one class to express car


# -*- coding='utf-8 -*-
class Car(object):

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        # print one massage of odometer
        print("This car has {0} miles on it.".format(str(self.odometer_reading)))

    def update_odometer(self, mileage):
        # set the mileage as a certain number
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        if miles >=0:
            self.odometer_reading += miles
        else:
            print("Can't increase minus number!")

class Battery():

    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a {} -kwh battery.".format(str(self.battery_size)))

    # def upgrade_battery(self):
    #     if self.battery_size != 85:
    #         self.battery_size = 85

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately {}".format(str(range))
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        # initialized father class
        super().__init__(make, model, year)
        self.battery = Battery()   # very import!!!
        
    
    # def describe_battery(self):
    #     # print one masseage of battery
    #     print("This car has a {0} -kw battery.".format(str(self.battery_size)))

    # def fill_gas_tank(self):
    #     # elctric car no tank
    #     print("This car doesn't need a gas tank!")
    

if __name__=='__main__':
    # my_new_car = Car('audi', 'a4', 2016)
    # print(my_new_car.get_descriptive_name())
    # my_new_car.read_odometer()
    # print('-------------')
    # my_new_car.update_odometer(23)
    # my_new_car.read_odometer()
    # my_used_car = Car('subaru', 'outback', 2013)
    # print(my_used_car.get_descriptive_name())
    # my_used_car.update_odometer(23500)
    # my_used_car.read_odometer()
    # my_used_car.increment_odometer(100)
    # my_used_car.read_odometer()
    my_tesla = ElectricCar('tesla', 'model s', 2016)
    print(my_tesla.get_descriptive_name())
    my_tesla.battery.describe_battery()
    print('----------------')
    my_tesla.battery.upgrade_battery()
    my_tesla.battery.get_range()


