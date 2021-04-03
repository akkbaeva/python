class VehicleWithMotor:
    def __init__(self, seat, pedal, motor):
        self.seat = seat
        self.pedal = pedal
        self.motor = motor

    def __str__(self):
        return f'{self.seat}, {self.pedal}, {self.motor}'


class VehicleWithoutMotor:
    def __init__(self, seat, pedal, chain):
        self.seat = seat
        self.pedal = pedal
        self.chain = chain

    def __str__(self):
        return f'{self.seat}, {self.pedal}, {self.chain}'


class Car(VehicleWithMotor):
    def ride(self):
        print('ridding')

class Bus(VehicleWithMotor):
    def passengers(self):
        print('a lot more seats')

class Bicycle(VehicleWithoutMotor):
    def need_more(self):
        print('need more')
