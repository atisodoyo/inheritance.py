class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am a {self.gender}.")

# Create an instance of the Person class
person = Person("Jane Odoyo", 23, "female")

# Call the introduce method to display the person's information
person.introduce()