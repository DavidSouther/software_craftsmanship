from math import pi

class Rug():
    def __init__(self, has_fringe = False):
        self.has_fringe = has_fringe 
        self.description = "basic"
    
    def get_values(self):
        """
        Ask the user for all the values necessary for this rug.

        Extending classes should call this before asking for their own inputs.
        """
        wants_fringe = input("Should this rug have fringe (y/N)? ")
        if wants_fringe.lower().startswith('y'):
            self.has_fringe = True

    def area(self):
        """ Calculate the area of the rug. To be implemented by an extending class. """
        return 0
    
    def perimeter(self):
        """ Calculate the perimeter of the rug. To be implemented by an extending class. """
        return 0

    def cost_per_area(self):
        """ Return the price per square foot of this type of rug. """
        return 5

    def cost_per_perimeter(self):
        """ Return the price per foot of perimeter for this type of rug. """
        return 1.5
    
    def cost(self):
        area_cost = self.area() * self.cost_per_area()
        if self.has_fringe:
            perimeter_cost = self.perimeter() * self.cost_per_perimeter()
        else:
            perimeter_cost = 0
        total_cost = area_cost + perimeter_cost
        return total_cost

    def print(self):
        price = self.cost()
        if self.has_fringe:
            with_fringe = "with"
        else:
            with_fringe = "without"

        print(f"This {self.description} rug costs ${price:.2f} {with_fringe} fringe.")

class SquareRug(Rug):
    def __init__(self, size = 0, has_fringe = False):
        super().__init__(has_fringe)
        self.side_length = size
        self.description = "square"
    
    def get_values(self):
        super().get_values()
        self.side_length = float(input("Side length of this square rug? "))

    def area(self):
        """ The area of a square is its side length squared. """
        return self.side_length ** 2

    def perimeter(self):
        """ The perimeter of a square is its side length four times. """
        return self.side_length * 4

class RectangularRug(Rug):
    def __init__(self, width = 0, length = 0, has_fringe = False):
        super().__init__(has_fringe)
        self.width =  width
        self.length = length 
        self.description = "rectangular"
    
    def get_values(self):
        super().get_values()
        self.width = float(input("Width of the rectangular rug? "))
        self.length = float(input("Length of the rectangular rug? "))

    def area(self):
        """ The area of a rectange is its length times its width. """
        return self.width * self.length

    def perimeter(self):
        """ The perimeter of a rectange is its twice its length plus twice its width. """
        return self.width * 2 + self.length * 2

class CircularRug(Rug):
    def __init__(self, radius = 0, has_fringe = False):
        super().__init__(has_fringe)
        self.radius = radius
        self.description = "circular"
    
    def get_values(self):
        super().get_values()
        self.radius = float(input("Radius of this circular rug? "))

    def area(self):
        """ The area of a circle is pi times its radius squared. """
        return pi * self.radius ** 2
    
    def perimeter(self):
        """ The perimeter of a circle is pi times its diameter. """
        return pi * self.radius * 2

def get_rug():
    print("1) Square Rug")
    print("2) Rectangular Rug")
    print("3) Circular Rug")
    rug_type = input("Which type of rug? ")
    if rug_type == "1":
        return SquareRug()
    elif rug_type == "2":
        return RectangularRug()
    elif rug_type == "3":
        return CircularRug()

def price_rug():
    rug = get_rug()
    rug.get_values()
    rug.print()

def price_rugs():
    while not input("Price another rug (Y/n): ").lower().startswith("n"):
        price_rug()

if __name__ == "__main__":
    price_rugs()