# 💻 Quick Practice Problem (Unit 2.1)
# Create a class Laptop with a class attribute warranty = "1 Year".
# Add a method set_specs(self, brand, ram) that stores brand and ram as instance attributes.
# Outside the class, create an object l1, call set_specs, and print l1's brand and the class warranty.

class Laptop():
    Warranty = "1 Year"

    def set_specs(self,brand,RAM):
        self.brand = brand
        self.RAM = RAM

    def print_specs(self):
        print(f"\nBrand : {self.brand} \nRAM : {self.RAM} \nWarranty : {self.Warranty}")


l1 = Laptop()
l1.set_specs("Lenovo","8GB")
l1.print_specs()

