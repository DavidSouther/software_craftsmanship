from math import pi

class Rug():
    def __init__(self, has_fringe = False, description = "", color=""):
        self.has_fringe = has_fringe 
        self.description = description
        self.color = color
    
    def get_values(self):
        """
        Ask the user for all the values necessary for this rug.

        Extending classes should call this before asking for their own inputs.
        """
        wants_fringe = input("Should this rug have fringe (y/N)? ")
        if wants_fringe.lower().startswith('y'):
            self.has_fringe = True
        self.color = input("What is the color of this rug? ")

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

        print(f"This {self.color} {self.description} rug costs ${price:.2f} {with_fringe} fringe.")

class RectangularRug(Rug):
    def __init__(self, width = 0, length = 0):
        Rug.__init__(self, description="rectangular")
        self.width = width
        self.length = length 
    
    def get_values(self):
        Rug.get_values(self)
        self.width = float(input("Width of the rectangular rug? "))
        self.length = float(input("Length of the rectangular rug? "))

    def area(self):
        """ The area of a rectange is its length times its width. """
        return self.width * self.length

    def perimeter(self):
        """ The perimeter of a rectange is its twice its length plus twice its width. """
        return self.width * 2 + self.length * 2

class SquareRug(RectangularRug):
    def __init__(self, size = 0, has_fringe = False):
        RectangularRug.__init__(self, size, size)
        self.side_length = 0
        self.description = "square"
    
    def get_values(self):
        Rug.get_values(self)
        side_length = float(input("Side length of this square rug? "))
        self.length = side_length
        self.width = side_length

class CircularRug(Rug):
    def __init__(self, radius = 0):
        Rug.__init__(self, description="circular")
        self.radius = radius
    
    def get_values(self):
        Rug.get_values(self)
        self.radius = float(input("Radius of this circular rug? "))

    def area(self):
        """ The area of a circle is pi times its radius squared. """
        return pi * self.radius ** 2
    
    def perimeter(self):
        """ The perimeter of a circle is pi times its diameter. """
        return pi * self.radius * 2

class Order():
    def __init__(self):
        self.rugs = []
        self.name = "" 
    
    def main(self):
        print("IncrediRugz Order Form")
        self.name = input("Preparing order for (name): ")
        while not input("Price another rug (Y/n): ").lower().startswith("n"):
            self.add_rug()
        
        self.print_summary()

    def add_rug(self):
        rug = make_rug()
        rug.get_values()
        self.rugs.append(rug)
        
    def print_summary(self):
        print()
        print(f"IncrediRugz order for {self.name}:")
        total = 0
        for rug in self.rugs:
            total += rug.cost()
            rug.print()
        
        print()
        print(f"{len(self.rugs)} rugs")
        print(f"Total: ${total:.2f}")
        print()

def make_rug():
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

if __name__ == "__main__":
    Order().main()
