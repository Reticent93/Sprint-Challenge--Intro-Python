# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle:
    pass


class FlightVehicle(Vehicle):
    pass


# inherits methods from Vehicle

class Starship(FlightVehicle):
    pass


# inherits from FlightVehicle which inherits from Vehicle


class GroundVehicle(Vehicle):
    pass


# inherits methods from Vehicle


class Car(GroundVehicle):
    pass


# inherits from GroundVehicle inherits from Vehicle

class Motorcycle(GroundVehicle):
    pass


# inherits from GroundVehicle inherits from Vehicle

class Airplane(FlightVehicle):
    pass

# inherits from FlightVehicle which inherits from Vehicle
