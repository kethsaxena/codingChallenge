class MyVehicle:
    def __init__(self, base_rate=10):
        self.__base_rate = base_rate

    def get_base_rate(self):
        return self.__base_rate  # Getter method for private variable

class Cycle(MyVehicle):
    def get_total_price(self):
        return self.get_base_rate()

class Car(MyVehicle):
    def __init__(self, base_rate=10, conv_fee=5):
        super().__init__(base_rate)
        self.conv_fee = conv_fee

    def get_total_price(self):
        return self.get_base_rate()+self.conv_fee 


# Example Usage
cycle = Cycle()  # Uses default base_rate = 10 from Vehicle
print("Cycle Total Price:", f"${cycle.get_total_price():0.2f}")

bike = Car()  # Uses default base_rate = 10, conv_fee = 5
print("Bike Total Price:", f"${bike.get_total_price():0.2f}")

# Override default base_rate and conv_fee in Bike
bike_custom = Car(base_rate=20, conv_fee=7)
print("Custom Bike Total Price:", f"${bike_custom.get_total_price():0.2f}")

# Override default base_rate in Cycle
cycle_custom = Cycle(base_rate=15)
print("Custom Cycle Total Price:", f"${cycle_custom.get_total_price():0.2f}")


