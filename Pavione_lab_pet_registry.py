# Define the base Pet class to store basic pet information
class Pet:
    def __init__(self, name, species, age):
        # Validate input for age to ensure it's not negative
        if not isinstance(age, (int, float)) or age < 0:
            raise ValueError("Age must be a non-negative number")
        self.name = name
        self.species = species
        self.age = age
    
    # Method to print a summary of the pet's details
    def describe(self):
        print(f"Name: {self.name}, Species: {self.species}, Age: {self.age}")

# Define the Dog subclass that inherits from Pet
class Dog(Pet):
    def __init__(self, name, age, breed):
        # Call the parent class constructor
        super().__init__(name, "Dog", age)
        self.breed = breed
    
    # Override describe to include breed
    def describe(self):
        print(f"Name: {self.name}, Species: {self.species}, Age: {self.age}, Breed: {self.breed}")
    
    # Method for dog-specific behavior
    def bark(self):
        print(f"Woof! My name is {self.name}.")

# Define the Cat subclass that inherits from Pet
class Cat(Pet):
    def __init__(self, name, age, color):
        # Call the parent class constructor
        super().__init__(name, "Cat", age)
        self.color = color
    
    # Override describe to include color
    def describe(self):
        print(f"Name: {self.name}, Species: {self.species}, Age: {self.age}, Color: {self.color}")
    
    # Method for cat-specific behavior
    def meow(self):
        print(f"Meow! My name is {self.name}.")

# Main program to demonstrate the pet registry
def main():
    # Create a list to store pets
    pets = []
    
    try:
        # Create Dog and Cat objects with different attributes
        dog1 = Dog("Buddy", 3, "Golden Retriever")
        cat1 = Cat("Whiskers", 2, "Tabby")
        dog2 = Dog("Max", 5, "Bulldog")
        
        # Add pets to the list
        pets.extend([dog1, cat1, dog2])
        
        # Call describe and unique methods for each pet
        print("Individual pet details:")
        dog1.describe()
        dog1.bark()
        cat1.describe()
        cat1.meow()
        dog2.describe()
        dog2.bark()
        
        # Print summary of all pets in the list
        print("\nAll pets in registry:")
        for pet in pets:
            pet.describe()
            
    except ValueError as e:
        print(f"Error: {e}")

# Run the main program
if __name__ == "__main__":
    main()