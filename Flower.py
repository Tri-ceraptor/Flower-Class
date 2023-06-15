class Flower:
    def __init__(self, name):
        self.name = name

    def grow(self):
        print("The " +self.name + " is growing.")

    def bloom(self):
        print("The " + self.name + " is blooming.")

def main():
    flower1 = Flower("Rose")
    flower1.grow()
    flower1.bloom()
    flower2 = Flower("Daisy")
    flower2.grow()
    flower2.bloom()

if __name__ == "__main__":
  main()
  
# This program defines a class called "Flower" with methods to simulate the growth and blooming of a flower. It creates two instances of the Flower class, one representing a "Rose" and the other a "Daisy", and calls the "grow()" and "bloom()" methods on each flower. When the script is run directly, the "main()" function is executed.

# by Oleksandr Vykliuk