#Question 4 implementation of the make_sound method

# Dog class
class Dog:
    def make_sound(self):
        return "Woof! Woof!"

# Cat class
class Cat:
    def make_sound(self):
        return "Meow!"

# Function that works with any object having make_sound()
def process_sound(sound_object):
    print(sound_object.make_sound())


if __name__ == "__main__":
    choice = input("Enter an animal (dog/cat): ").strip().lower()

    if choice == "dog":
        animal = Dog()
    elif choice == "cat":
        animal = Cat()
    else:
        print("Invalid choice! Please enter either 'dog' or 'cat'.")
        exit()

    process_sound(animal)
