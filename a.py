class Car:
    def __init__(self,model,color,seats):
        self.model = model
        self.color = color
        self.seats = seats

    def type_of_car(self):
        print(
            "Model: " + self.model + "\n" +
            "Color: " + self.color + "\n" +
            "Seats: " + self.seats)

c1 = Car("HondaCivic", "Blue", "4")
c2 = Car("Tesla", "Silver", "4")
c3 = Car("Solstice", "Yellow", "2")

c1.type_of_car()
print()
c2.type_of_car()
print()
c3.type_of_car()