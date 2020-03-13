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

# Base class

class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class FlightVehicle(Vehicle):
    def __init__(self, name, color, size)
    super().__init__(name, color)
    self.size = size

class Starship(FlightVehicle):
    def __init__(self, name, color, size, engine)
    super().__init__(name, color, size)
    self.engine = engine

class Airplane(FlightVehicle):
    def __init__(self, name, color, size, wings)
    super().__init__(name, color, size)
    self.wings = wings

class GroundVehicle(Vehicle):
    def __init__(self, name, color, tires)
    super().__init__(name, color)
    self.tires = tires

class Car(GroundVehicle):
    def __init__(self,name, coloe, tires, axel)
    super().__init__(name, color, tires)
    self.axel = axel

class Motorcycle(GroundVehicle):
    def __init__(self, name, color, tires, seats)
    super().__init__(name, color, tires)
    self.seats = seats

