class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    # Method overriding
    def speak(self):
        print("Dog barks")

# Example
a = Animal()
d = Dog()

a.speak()  # Output: Animal makes a sound
d.speak()  # Output: Dog barks
