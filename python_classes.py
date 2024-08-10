# Create a class template

# self parameter is a reference to the current instance of the clas, and it is used
# to access variables that belong to the class.

class Car:
    sound = "pinpin!"
    def __init__(self, brandName, year, color, plateNumber):
        self.brandName = brandName
        self.year = year
        self.color = color
        self.plateNumber = plateNumber

    def makeSound(self, sound = sound):
        print(f"Hello, {sound}")

    def __str__(self):
        return f"Brand: {self.brandName}, Year: {self.year}, Color: {self.color}, Plate Number: {self.plateNumber}"

def main():

    # object instances of the Car class
    toyota = Car("Toyota", "2007", 'black', 'AZ675LAG')

    honda = Car("Honda", "2019", 'silver', 'DG356ABJ')

    honda.makeSound()
    toyota.makeSound("pehpeh!")

    honda.year = "2024"
    del honda

    print(honda.brandName, honda.year, honda.color)

if __name__ == "__main__":
    main()