class DistanceConversion:
    def __init__(self, meter):
        self.__meter = meter

    def centimeter(self):
        return self.__meter * 100

    def kilometer(self):
        return self.__meter / 1000

    def inches(self):
        return self.__meter * 39.37

    def display(self):
        print(f"meter to centimeter", self.centimeter())
        print(f"meter to kilometer", self.kilometer())
        print(f"meter to inch", self.inches())

meter = float(input("meter: "))
distance = DistanceConversion(meter)
distance.display()